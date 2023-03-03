# Staff项目

## 简介

staff 应用程序，用于展示员工信息列表。此项目使用Python的Flask框架，SQLite数据库和Bootstrap前端框架开发。

## 设计

### 数据库设计

该应用程序使用SQLite数据库存储员工信息数据。具体的数据库设计如下：

#### staff_information表

| 列名               | 类型     | 描述                 |
| ------------------| --------|----------------------|
| employeeid         | INTEGER | 员工ID               |
| lastname           | TEXT    | 员工姓氏             |
| firstname          | TEXT    | 员工名字             |
| gender             | TEXT    | 员工性别             |
| email              | TEXT    | 员工邮箱             |
| phonenumber        | TEXT    | 员工电话号码         |
| city               | TEXT    | 员工城市             |
| state              | TEXT    | 员工州               |
| zip                | TEXT    | 员工邮编             |
| username           | TEXT    | 员工用户名           |
| password           | TEXT    | 员工密码             |
| department         | TEXT    | 员工所在部门         |
| jobtitle           | TEXT    | 员工职位             |
| employeestatus     | TEXT    | 员工雇佣状态         |
| dateofhire         | TEXT    | 员工雇佣日期         |
| dateoftermination  | TEXT    | 员工离职日期         |
| age                | INTEGER | 员工年龄             |
| maritalstatus      | TEXT    | 员工婚姻状况         |
| education          | TEXT    | 员工教育程度         |
| joblevel           | INTEGER | 员工职位级别         |
| jobrole            | TEXT    | 员工职位角色         |
| jobroletype        | TEXT    | 员工职位类型         |
| businessunit       | TEXT    | 员工所在业务部门     |
| managementlevel    | INTEGER | 员工管理级别         |
| travel             | TEXT    | 员工差旅情况         |

#### staff_privacy_information表

| 列名                        | 类型     | 描述                 |
| ---------------------------| --------|----------------------|
| employeeid                  | INTEGER | 员工ID               |
| attrition                   | TEXT    | 员工是否离职         |
| distancefromhome            | INTEGER | 员工家与公司距离     |
| educationfield              | TEXT    | 员工所学专业         |
| monthlyincome               | INTEGER | 员工月收入           |
| numcompaniesworked          | INTEGER | 员工曾经工作的公司数 |
| over18                      | TEXT    | 员工是否年满18岁     |
| percentsalaryhike           | INTEGER | 员工薪资提高百分比   |
| standardhours               | INTEGER | 员工标准工时         |
| stockoptionlevel            | INTEGER | 员工股票期权级别     |
| totalworkingyears           | INTEGER | 员工工作年限         |
| trainingtimeslastyear       | INTEGER | 员工上一年的培训次数 |
| yearsatcompany              | INTEGER | 员工在公司工作年限   |
| yearsincurrentrole          | INTEGER | 员工在当前职位工作年限 |
| yearssincelastpromotion     | INTEGER | 员工距离上次升职年限 |
| yearswithcurrmanager        | INTEGER | 员工与当前经理共事年限 |

### 前端设计

该应用程序使用Bootstrap前端框架设计，并包括以下页面：

- index.html：用于显示员工列表。
- detail.html：用于显示员工的详细信息。
- chat_detail.html：用于展示聊天机器人的反馈结果。

### 后端设计

该应用程序使用Python的Flask框架设计，包括以下组件：

- Flask应用程序：用于处理HTTP请求和响应。
- SQLite数据库：用于存储员工信息和员工隐私信息数据。
- OpenAI库：用于自然语言处理和生成智能聊天记录。

### 开发

在开发 staff 项目时，我们完成了以下任务：

编写前端代码：使用 Bootstrap 前端框架设计了员工信息展示页面和聊天机器人页面。
实现后端逻辑：使用 Flask 框架实现了后端逻辑，包括处理 HTTP 请求和响应、连接 SQLite 数据库、调用 OpenAI API 进行人工智能交互功能的实现。
编写测试用例：使用 Behave 进行自动化测试，编写了测试用例以测试应用程序的功能和性能。

### 实施
在部署 staff 项目时，我们完成了以下任务：

安装依赖项：使用 Pyenv 和虚拟环境管理工具，安装并配置了 Flask、Flask Paginate、Behave、Selenium 和 Gunicorn 等 Python 依赖项。
初始化数据库：使用 parse_csy.py 脚本初始化 SQLite 数据库，并导入员工信息数据和员工隐私信息数据。
启动应用程序：使用 Gunicorn 运行 Flask 应用程序，确保在后台持续运行。
访问应用程序：在 Web 浏览器中访问应用程序的 URL，以查看员工信息和与聊天机器人进行智能对话。

#### 单元测试
该项目使用 Behave 和 Selenium 进行自动化测试，可以使用以下命令运行测试：

behave

测试用例位于 features 文件夹下。