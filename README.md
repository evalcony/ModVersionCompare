# ModVersionCompare
比较mod不同版本之间的文件差异，可以精确到行

### 注意事项
- 需要比对文件编码格式是 `utf-8`。
- 文件名全部转小写。

### 使用方法

1. 初始化
```
. init_shell.sh
```

2. 执行
```
python3 compare.py -d1 mod1路径 -d2 mod2路径 -mode simple
```

#### 参数解释

-h 帮助

-mode: 有两个值
`simple` 简版模式，只比较有效总行数差异
`detail` 详版模式，精细到行差异

-d1 mod1路径。从namespace下一级开始填。比如，mod放在目录 `resource/EdwinRomance/output/` 目录下，则只需要填 `output`。d2同理。
`EdwinRomance` 在 `appconf.ini` 中的 `namespace` 中设置。

-d2 mod2路径。