# 一.创建仓库	

`git init` 仓库初始化

`git status` 查看当前状态（新增、修改、删除）

# 二.添加文件到暂存区

`git add <file1> <file2>` 

`git add .` 添加所有程序到暂存区

# 三.提交	

`git commit -m "提交说明"` 提交到本地仓库

`git push origin main` 推送到远程仓库

# 四.取消追踪

`git rm <filepath>` 文件会从工作区（磁盘）和 Git 仓库中都被删除

`git rm --cache <filepath>` 文件仍保留在磁盘中,Git 不再跟踪它的变化

# 五.项目历史

`git log` 显示提交记录（从最近到最早）

`git log --oneline` 每条提交显示为一行：`<短哈希> <提交说明>`

`git log --oneline --graph --all` 图形化查看分支历史

`git show <提交哈希>` 查看某次提交的具体改动

`git blame <filename>` 快速定位某个文件是谁写的

# 六.撤回

`git reset --hard <提交哈希>` 回退到任意历史版本

```c
--hard  工作区和暂存区都清除
--soft  工作区和暂存区都不清除
不带参数默认使用--mixed 工作区保留 暂存区清除 
```



# 七.gitignore

`.gitignore` 是 Git 用来忽略某些文件或文件夹的配置文件。它告诉 Git：**“这些文件不要纳入版本控制。”**

.gitignore文件需要自己手动创建`touch .gitignore` 

STM32 项目常用 `.gitignore`

```c
# 编译产物
*.o
*.elf
*.bin
*.hex
*.map
*.lst

# 编译输出目录
build/
Debug/
Release/

# IDE 配置
.vscode/
.idea/
*.launch
*.uvoptx
*.uvprojx
*.cproject
*.project
*.settings/

# 日志和临时文件
*.log
*.tmp
*.bak
*.swp
```

# 八.分支

分支就是对项目代码的一条“独立发展线”。你可以在分支上自由修改、提交，而不会影响主线（通常是 `main` 或 `master`）。等你开发完成，再把分支合并回主线。

1. 创建分支

   ` git branch <分支名>` 

2. 切换分支

   `git switch <branchname>` 

3. 删除分支

   `git branch -d <分支名>`      # 删除已合并的分支
   `git branch -D <分支名>`      # 强制删除（未合并也删）

4. 合并分支

   `git switch main` #切换为主分支

   `git merge <branchname>` #合并目标分支

5. 推送分支到远程仓库

   `git push origin <分支名>` 

6. 查看分支

   `git branch` #查看本地分支

   `git branch -r` #查看远程分支

   `git branch -a` #查看所有分支(本地+远程)

# 九.推送和拉取

`git push origin <branchname>` #推送

例如`git push origin main`

`git pull origin <branchname>` #拉取

例如`git pull origin main` 

# 十.如何找回丢失的提交

输入`git reflog` 

会看到类似:

```c
b1c2d3e HEAD@{0}: reset: moving to B
e5f6g7h HEAD@{1}: commit: 修复 PID 控制器
...
```

然后使用

```c
git reset --hard 哈希值
```

# 十一.子仓库

子仓库是嵌套的独立的仓库,克隆时分支可以直接切换,而子模块需要额外初始化和更新

```c
git submodule init
git submodule update
```



