# -*- coding: utf-8 -*-

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 04",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 04 
===================================================

Le but de ce module est de montrer comment créer ou modifier des menus dans l'interface.

Ce module installe le module CRM pour pouvoir manipuler ces menus


""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',
  "depends" : ["base","crm"],  # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
  "init_xml" : [],             # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],             # Liste des fichiers XML à installer pour charger les données de démonstration
  "update_xml" : [],           # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)
  "installable": True,         # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False              # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}




