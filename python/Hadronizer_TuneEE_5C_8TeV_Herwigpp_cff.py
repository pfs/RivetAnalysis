import FWCore.ParameterSet.Config as cms

from Configuration.Generator.HerwigppDefaults_cfi import *
from Configuration.Generator.HerwigppUE_EE_5C_cfi import *
from Configuration.Generator.HerwigppPDF_CTEQ6_LO_cfi import *									# Import CTEQ6L PDF as shower pdf
from Configuration.Generator.HerwigppPDF_NNPDF30_NLO_cfi import herwigppPDFSettingsBlock as herwigppHardPDFSettingsBlock 	# Import NNPDF30 NLO as PDF of the hard subprocess
from Configuration.Generator.HerwigppEnergy_8TeV_cfi import *
from Configuration.Generator.HerwigppLHEFile_cfi import *
from Configuration.Generator.HerwigppMECorrections_cfi import *

generator = cms.EDFilter("ThePEGHadronizerFilter",
	herwigDefaultsBlock,
	herwigppUESettingsBlock,
	herwigppPDFSettingsBlock,
	herwigppHardPDFSettingsBlock,			# Implementing renamed NNPDF30 config block
	herwigppEnergySettingsBlock,
	herwigppLHEFileSettingsBlock,
	herwigppMECorrectionsSettingsBlock,

	configFiles = cms.vstring(),
	parameterSets = cms.vstring(
		'hwpp_cmsDefaults',
		'hwpp_ue_EE5C',
		'hwpp_cm_8TeV',
		'hwpp_pdf_CTEQ6L1',			# Shower PDF matching with the tune
		'hwpp_pdf_NNPDF30NLO_Hard',		# PDF of hard subprocess
		'hwpp_LHE_Powheg_DifferentPDFs',
		'hwpp_MECorr_Off',			# Switch off ME corrections while showering LHE files as recommended by Herwig++ authors
	),

        crossSection = cms.untracked.double(-1),
        filterEfficiency = cms.untracked.double(1.0),
)
ProductionFilterSequence = cms.Sequence(generator)
