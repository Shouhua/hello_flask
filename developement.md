## 前端、后端的概念
- 很早以前大多的设计采用的是C/S(client/server)模式，大多需要电脑提供的原生能力，比如IO，自定义协议等，目前工控行业还有很多类似软件，尝试用MFC、winform、wpf等windows常用的框架。
- B/S模式通常指的是Browser/Server，维护server，通过浏览器进行操作，只要有合适浏览器版本就可能使用。
本质上来说没有区别，浏览器也是client端上的软件，只不过可以通过http协议互动。  
今天主要是聊下B/S模式下开发。web开发也是有发展历程的，早期javascript使用场景仅仅限于form表单的处理等，web开发一般采用服务端渲染的方式，比如asp，jsp等，随着nodejs的推出，javascript的场景扩大到服务端应用、浏览器能力越来越强大、以及前端需求场景越来越多样化，前后端分离，后端服务主要提供RESTful风格接口，前端主要渲染数据。
目前后端服务有多种选择，比如java的spring boot，.net的asp.net core, nodejs里面的express，python-flask等。前端框架主要有vuejs，reactjs，angular等
## 软件研发过程
开发写代码只是软件开发中的一环，整个过程如果配置齐全会涉及到多个部门和小组的参与，所以公司体量越大，沟通成本会越高，这个也是很多创业公司中必然碰到和解决的问题。如果配置齐全的话，前期还有销售，售前，方案设计等部门的参与。
- 确认需求(需求文档) 白话说就是要干什么，实现什么功能，功能要达到什么指标  
- 技术调研（设计） 根据需求梳理哪些需要提前技术调研的，能不能实现，实现的成本，比如需要那些软硬件环境支持，需要多少工时完成  
- 界面设计(UE设计) 软件中view部分的设计  
- 服务侧设计（业务架构/数据库/缓存等）  
- 编排设计 比如目前流行的容器化服务，需要安排各种镜像以及镜像的编排  
- 研发 流程管理跟踪，分工开发  
- 测试  
- 发布(部署文档)  
## 研发中使用的技术栈及工具
虽然coding的部分是流程中的一环，但是我们参与最多的大多是这一环，技术栈有很多，选取一定要符合自己的需求设计。有的本来是很简单的几个用户的管理系统，非要尝试上微服务架构，浪费人力物力，还增加了后期维护成本。技术栈的设计也是迭代的过程，首先满足需求，然后随着需求的增加或者变更，调整自己的架构设计，更有甚者需要更换技术栈满足要求，很多创业公司刚开始的时候选取快速形成MVP的技术栈，然后扩张之后再更新比较支撑大型服务的技术栈。  
- uber数据库从postgresql迁移至mysql：https://eng.uber.com/postgres-to-mysql-migration/  
- 京东从以前的.net framework技术栈迁移至java等  
下面就研发流程中遇到的情况讨论下：
- 典型的架构  
架构例子 https://github.com/dotnet-architecture/eShopOnContainers/blob/dev/img/eShopOnContainers-architecture.png
- 代码仓库与版本管理  
使用过的有SVN、git，目前比较流行的就是git（https://zh.wikipedia.org/wiki/Git），基于git形成了github，gitlab、gitee等大型的开源仓库，繁荣了开源文化。  
本地开发的时候，git的仓库可以使用github的私有仓库，然后在上面进行issue和流程管理；还可以部署gitlab开源的软件gitlab-ce，继承了git flow和部署相关的流程。相关的文档：  
pro git https://git-scm.com/book/zh/v2  
git client https://git-scm.com/download/gui/windows  
- 需求管理  
- 前后端交互  
前后端交互主要是通过http接口，为了能同时进行开发，需要有一套有共识的沟通工具。可以使用swagger，也可以使用YAPI管理多个工程的接口，开源可以本地部署。  
YAPI https://github.com/YMFE/yapi  
- 后端开发环境  
开发工具：Vscode、Pycharm  
Python https://www.liaoxuefeng.com/wiki/1016959663602400  
Python Flask  
MySQL  
Redis  
RESTful http://restful.p2hp.com/ https://www.ruanyifeng.com/blog/2014/05/restful_api.html  
https://docs.github.com/en/rest  
- 前端开发环境  
开发工具: Vscode（推荐）, Atom, Webstorm等  
Vue3 https://staging-cn.vuejs.org/guide/introduction.html https://vuejs.org/  
http协议 https://developer.mozilla.org/zh-CN/docs/Web/HTTP  
- 调试工具  
web调试工具可以使用curl、postman  
- 部署环境  
docker https://dockone.io/article/389  
docker registry  
docker https://yeasy.gitbook.io/docker_practice/  
docker compose  
- 线上交流工具等  
## 数据库需要注意的问题
- 数据库主从库，比如主库负责客户端读取，从库负责写入
- 数据库同步程序失败预警（邮件，钉钉等）
- 断电重启
