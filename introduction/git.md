<h1 style='text-align: center'>Git 版本控制</h1>

### git配置用户信息

- 配置用户信息

  ```shell
  git config --global user.name "[yourName]"
  git config --global user.email "[yourEmail@domain.com]"
  ```

- 查看用户信息
  `git config --list`

---

### git区域

- 工作区 working directory
- 暂存区 staging area
- 本地仓库 local repository
- 远程仓库 remote repository

---

### git 名词

- 提交 
- 推送
- 变基
- 合并

---

### git 状态

- Untracked：未跟踪，没有被git管理
- Tracked：跟踪，被git管理
  - Added：第一次被添加
  - Modified：提交后又修改过
  - Staged：已经添加到暂存区，但还没有提交

---

### git 命令

- `git init` 初始化git仓库

- `git add [filename]` 添加filename文件到暂存区
- `git commit -m "[提交说明]"` 将暂存区文件提交到本地仓库
- `git add .` 添加所有文件（U、M）到暂存区
- `git push` 将本地仓库提交到远程仓库
- `git pull` 将远程仓库更新到本地仓库
- `git rm [filename]` 删除文件（暂存区、取消版本管理），但是还在.git里
- `git status` 显示git所有文件状态
- `git status -s` 显示git所有文件状态（简略）

- `git ls-files` 查看暂存区文件列表

- `git log` 查看提交记录
- `git log --oneline` 查看提交记录，只显示hash和提交说明
- `git checkout [hash]` 回退到指定提交记录，hash为提交记录的hash值
- `git reset --hard [hash]` 回退到指定提交记录，覆盖掉工作区和暂存区

- `git branch` 查看所有分支
- `git bransh [branchName]` 为一个本地仓库创建分支，branchName为分支名
- `git switch [branchName]` 切换分支，branchName为分支名，之后git push就会提交到该分支，会覆盖掉其他分支的工作区的文件
- `git merge [branchName]` 将branchName分支合并到当前分支，head指向当前分支和branchName
- `git branch -d [branchName]` 删除branchName分支

- `git remote add [remoteName] [https://github.com/[username]/[repository].git` 添加远程仓库，remoteName为远程仓库名
- `git push -u [remoteName] [branchName]/master` 将本地仓库提交到远程仓库，branchName为分支名，如果没有该branch，远程就会创建该branch

- `git clone [https://github.com/[username]/[repository].git` 克隆远程仓库到本地仓库，工作区也克隆
- `git pull [remoteName] [branchName]` 拉取远程仓库到本地仓库，工作区也拉取

---

### .gitignore 配置忽略版本控制文件

`.gitignore`是一个文件名

#### 为仓库配置.gitignore

- 配置全局.gitignore
  `git config --global core.excludesfile ~/.gitignore`
- 为单个仓库配置.gitignore
  将`.gitignore`文件放在仓库根目录下
- 为单个文件夹配置.gitignore
  将`.gitignore`文件放在文件夹目录下

#### 配置内容

- 常用忽略

  ```gitignore
  # 忽略 IDE 和编辑器生成的文件
  .idea/
  .vscode/

  # 忽略编译生成的文件和目录
  build/
  dist/

  # 忽略密钥文件
  .pem
  .cer

  # 忽略库
  lib/

  # 忽略日志文件
  *.log

  # 忽略操作系统生成的文件
  .DS_Store
  Thumbs.db
  ```

- python 常用忽略

  ```gitignore
  # 忽略python的venv虚拟环境
  venv/

  # 忽略 Python 编译文件
  *.pyc
  __pycache__/
  ```

---

### 私有远程仓库权限

- 管理员
- 开发者
- 观察员
- 报告员

### 远程链接地址

- https
- ssh
