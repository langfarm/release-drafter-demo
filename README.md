# release-drafter 练习

## 开发

### monorepo 项目结构

参数：https://github.com/carderne/postmodern-mono

### 准备环境

```bash
# 安装uv
brew install uv

# 设置 pypi 镜像
# vi ~/.zshrc
export UV_DEFAULT_INDEX="http://mirrors.aliyun.com/pypi/simple/"

# 不下载 python
# vi ~/.zshrc
# export UV_PYTHON_DOWNLOADS=never

# 下载依赖
uv sync
```


### 运行
```bash
# 代码格式化
uv run poe fmt

# 代码检查
uv run poe lint

# pyright 检测
uv run poe check

# 测试
uv run poe test


# 运行 python 代码
uv run python apps/tracing/tests/test_adder.py
```