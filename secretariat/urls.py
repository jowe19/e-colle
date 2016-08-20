#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = [
url(r'^$', views.connec, name="login_secret"),
url(r'^action$', views.action, name="action_secret"),
url(r'^action/resultats$', views.resultats, name="resultats_secret"),
url(r'^action/resultatcsv/(\d+)/(\d+)/(\d+)/(\d+)$', views.resultatcsv, name="resultatcsv_secret"),
url(r'^action/colloscope/(\d+)$', views.colloscope, name="colloscope_secret"),
url(r'^action/colloscope/(\d+)/(\d+)/(\d+)$', views.colloscope2, name="colloscope2_secret"),
url(r'^action/colloscopepdf/(\d+)/(\d+)/(\d+)$', views.colloscopePdf, name="colloscopepdf_secret"),
url(r'^action/colloscope/modifier/(\d+)/(\d+)/(\d+)$', views.colloscopeModif,name="colloscopemodif_secret"),
# url(r'^action/planification$', views.planification, name="planification"),
# url(r'^action/dispo$', views.dispo, name="dispo"),
# url(r'^action/dispo/modif/(\d+(?:-\d+)*)$', views.dispomodif, name="dispo_modif"),
# url(r'^action/frequence$', views.frequence, name="frequence"),
# url(r'^action/frequence/modif/(\d+)$', views.frequencemodif, name="frequence_modif"),
# url(r'^action/colles$', views.colles, name="colles"),
# url(r'^action/collesmodif/(\d+)$', views.collesmodif, name="collesmodif"),
# url(r'^action/edt$', views.edt, name="edt"),
url(r'^action/creneau/modifier/(\d+)/(\d+)/(\d+)$', views.creneauModif,name="creneaumodif_secret"),
url(r'^action/creneau/supprimer/(\d+)/(\d+)/(\d+)$', views.creneauSuppr,name="creneausuppr_secret"),
url(r'^action/creneau/dupliquer/(\d+)/(\d+)/(\d+)$', views.creneauDupli,name="creneaudupli_secret"),
url(r'^action/colloscope/ajax/(\d+)/(\d+)/(\d+)/(\d+|semaine)/(\d+|creneau)$', views.ajaxcolloscope,name="ajax_secret"),
url(r'^action/colloscope/ajax/eleve/(\d+)/(\d+)/(\d+)/(\d+|semaine)/(\d+|creneau)/(\w{2,3})$', views.ajaxcolloscopeeleve,name="ajax_secret_eleve"),
url(r'^action/colloscope/ajax/compat/(\d+)$', views.ajaxcompat,name="ajaxcompat_secret"),
url(r'^action/colloscope/ajax/majcolleur/(\d+|matiere)/(\d+)$', views.ajaxmajcolleur,name="ajaxmaj_secret"),
url(r'^action/colloscope/ajax/effacer/(\d+|semaine)/(\d+|creneau)$', views.ajaxcolloscopeeffacer,name="ajaxeffacer_secret"),
url(r'^action/colloscope/ajax/multi/(\d+|matiere)/(\d+|kolleur)/(\d+|groupe)/(\d+|eleve)/(\d+|semaine)/(\d+|creneau)/([1-9]{1}|[1-2]{1}[0-9]{1}|30|duree)/(1|2|3|4|8|frequence)/([1-9]{1}|1[0-9]{1}|20|permu)$', views.ajaxcolloscopemulti,name="ajaxmulti_secret"),
url(r'^action/colloscope/ajax/multi/confirm/(\d+|matiere)/(\d+|kolleur)/(\d+|groupe)/(\d+|eleve)/(\d+|semaine)/(\d+|creneau)/([1-9]{1}|[1-2]{1}[0-9]{1}|30|duree)/(1|2|3|4|8|frequence)/([1-9]{1}|1[0-9]{1}|20|permu)$', views.ajaxcolloscopemulticonfirm,name="ajaxmulticonfirm_secret"),
url(r'^action/groupe/(\d+)$', views.groupe,name="groupe_secret"),
url(r'^action/groupe/supprimer/(\d+)$', views.groupeSuppr,name="groupesuppr_secret"),
url(r'^action/groupe/modifier/(\d+)$', views.groupeModif,name="groupemodif_secret"),
url(r'^action/recapitulatif$', views.recapitulatif, name="recapitulatif"),
url(r'^action/ramassage$', views.ramassage, name="ramassage"),
url(r'^action/ramassage/suppr/(\d+)$', views.ramassageSuppr, name="ramassagesuppr"),
url(r'^action/ramassage/pdf/(\d+)$', views.ramassagePdf, name="ramassagepdf"),
url(r'^action/ects/credits/(\d+)$', views.ectscredits,name="secret_ects_credits"),
url(r'^action/ects/fiche/(\d+)$', views.ficheectspdf,name="secret_ects_fiche"),
url(r'^action/ects/attestation/(\d+)$', views.attestationectspdf,name="secret_ects_attestation"),
url(r'^action/ects/fiche/classe/(\d+)$', views.ficheectsclassepdf,name="secret_ects_fiche_classe"),
url(r'^action/ects/attestation/classe/(\d+)$', views.attestationectsclassepdf,name="secret_ects_attestation_classe")]