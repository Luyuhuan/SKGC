_base_ = [
    '../_base_/datasets/imagenet_bs64_swin_224.py',
    '../_base_/schedules/imagenet_bs1024_adamw_swin.py',
    '../_base_/default_runtime.py',  
]

model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='XCiT',
        patch_size=16,
        embed_dims=128,
        depth=12,
        num_heads=4,
        mlp_ratio=4,
        qkv_bias=True,
        layer_scale_init_value=1.0,
        tokens_norm=False,
        out_type='cls_token',
    ),
    head=dict(
        type='LinearClsHead',
        num_classes=2,
        in_channels=128,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
    ),
    train_cfg=dict(augments=[
        dict(type='Mixup', alpha=0.8),
        dict(type='CutMix', alpha=1.0),
    ]),
)

# dataset settings
train_dataloader = dict(batch_size=128)
