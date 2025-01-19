# release-drafter 练习

## 开发

### monorepo 项目结构

参考：https://github.com/carderne/postmodern-mono 创建 monorepo 项目结构。

### 准备 uv 环境

```bash
# 安装uv
brew install uv

# 设置 pypi 镜像
# vi ~/.zshrc
export UV_DEFAULT_INDEX="http://mirrors.aliyun.com/pypi/simple/"

# 不下载 python
# vi ~/.zshrc
# export UV_PYTHON_DOWNLOADS=never
```

### 安装依赖
```bash
# git clone 源码
git clone https://github.com/langfarm/release-drafter-demo.git

cd release-drafter-demo

# 创建虚拟环境 python3.11
uv venv -p 3.11

# 下载所有依赖, mono 内的项目也会增加到 python_path 里。
uv sync --all-packages
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

# 引入 .venv 环境
source .venv/bin/activate
# 直接 python 运行代码
python apps/tracing/tests/test_adder.py
```