from odoo import models, fields, api


class TodoTaskLine(models.Model):
    _name = 'todo.task.line'
    _description = 'Task Line Item'

    name = fields.Char()

    todo_task_id = fields.Many2one('todo.task')

