{
    'name': 'MyOdoo - Investments',
    'summary': 'MyOdoo - Investments',
    'description': '''
    Moduł szkoleniowy dla MyOdoo.pl.
    ''',
    'author': 'myOdoo.pl',
    'website': 'https://myodoo.pl',
    'category': 'Templates',
    'version': '1.0',
    'depends': [
        'base',
        'account',
        'sale', 
        'contacts'
    ],
    'data': [
        'report/investor_report_caller.xml',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/investor_report_view.xml'
    ],
    'installable': True,
    'auto_install': False
}