# pairwise-abr-ladder

## 领域

游戏、图形与多媒体

## 主题

自适应码率阶梯

## 说明

按内容定码率、GOP 对齐、滞回切换与清单带宽。

初始状态下 `media/abr_ladder.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
