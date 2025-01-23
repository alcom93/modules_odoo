{
    'name': "Gestion des employés",
    'version': '1.0',
    'depends': ['base', 'website'],
    'author': "NASSIF",
    'category': 'Human Ressources',
    'description': """
    Généreration de contrat, badge avec qr code
    """,
    'sequence': -1000,
    'data': [
        'security/ir.model.access.csv',
        'views/employe.xml',
        'report/employe_report.xml',
        'report/employe_report_template.xml',
        'report/fiche_report.xml',
        'report/fiche_report_template.xml',

    ],
    'installable':True,
    'application':True,
    'auto_install':False,
}