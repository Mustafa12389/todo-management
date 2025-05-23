{
     'name': "Todo Task",
     'author': "Mustafa Sayed",
     'category': '',
     'version': '17.0.0.1.0',
     'depends': ['base','mail'],
     'data': [
         'security/ir.model.access.csv',
         'views/base_menu.xml',
         'views\Todo_Task.xml',
         'views/todo_task_line_views.xml',
     ],
     'application': True,
 }