from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'To-Do Task'

    name = fields.Char(string="Task Name", required=True, default='new')
    description = fields.Text(string="Description", tracking=True)
    assign_to = fields.Many2one('res.users', string="Assigned To")
    date_availability = fields.Date(tracking=True)
    estimated_time = fields.Many2one(string="Estimated Time (Hours)")
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new')

    line_ids = fields.One2many('todo.task.line', 'todo_task_id')

    def action_in_progress(self):
        for record in self:
            record.state = 'in_progress'

    def action_new(self):
        for record in self:
            record.state = 'new'

    def action_completed(self):
        for record in self:
            record.state = 'completed'




