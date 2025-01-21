{
    'name': "Gestion des employés",
    'version': '1.0',
    'depends': ['base'],
    'author': "Ousmane",
    'category': 'Human Ressources',
    'description': """
    Généreration de contrat, badge avec qr code
    """,
    'sequence': -1000,
    'data': [
        'security/ir.model.access.csv',
        'views/employe.xml',
        'report/contrat_report.xml',
        'report/contrat_report_template.xml',
        'report/employe_report.xml',
        'report/employe_report_template.xml',

    ],
    'installable':True,
    'application':True,
    'auto_install':False,
}