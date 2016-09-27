import FWCore.ParameterSet.Config as cms

"""
"""
def getSamples(tag):
    samples=[]
    if tag=='TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8':
        samples=[
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/28BD6303-0C6A-E611-A876-0CC47A13D16E.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/28C6C19F-FE69-E611-8075-A0369F6367C2.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/28D456D6-0B6A-E611-99C2-1418776375C9.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/28EBB663-E969-E611-8971-A0000420FE80.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2A166B7C-176A-E611-8E4C-A0000420FE80.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2A3711DE-116A-E611-92AF-001E67248331.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2A5936FB-F869-E611-9CC7-0025905C2CB8.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2A709C93-066A-E611-8825-14187763B750.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2A72841E-0A6A-E611-9038-0CC47A4D769E.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2AA1489E-F169-E611-9531-001E67E6F841.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2AA6F44D-F069-E611-A214-B499BAAC0626.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2AF1A7EA-136A-E611-A86E-B083FEC76567.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2C08CCB4-FD69-E611-AC30-38EAA78D8FB0.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2C13C862-E969-E611-9540-0002C94D5518.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2CA02B3F-F969-E611-A2B8-0025905C2CBE.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2CA7CBB0-F969-E611-B317-0025905C43EC.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2CBEAF6B-E969-E611-AD67-FA163E32E934.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2E79F6B6-0D6A-E611-BFBC-0025905A6104.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2E846CEB-F869-E611-BD5F-549F35AF44A2.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2E8F8EC6-096A-E611-95F4-FA163EAF27D3.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2E9D8CCD-F169-E611-AA40-C4346BC75558.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2EA04F96-FE69-E611-A4EC-10983627C3CE.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2ECCDD74-106A-E611-911D-6C3BE5B51168.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2ED5EA47-FA69-E611-BF35-5065F381E211.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/2EE4A2FD-046A-E611-BCBF-001E67396FA9.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/301FBB2D-166A-E611-B4C7-FA163EF2A9F8.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/302473A8-1A6A-E611-A78D-0025905A48E4.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/3029BB14-026A-E611-A1E2-02163E016442.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/303F7C36-0E6A-E611-912A-0025905C2CD0.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/308CDB19-066A-E611-AF35-001E67396D56.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/309DB2F0-056A-E611-B0D2-10983627C3E8.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/3221DD77-0A6A-E611-8726-6C3BE5B5A308.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/322FFE98-F169-E611-9FD6-001E67E6F805.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/32599D42-066A-E611-B4A8-001E67581344.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/32BB25BB-FD69-E611-AD29-0CC47AA98B8C.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/32F252E4-0B6A-E611-884D-02163E014886.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/34251EA7-076A-E611-A312-7CD30AB7F7D8.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/342CC364-E969-E611-A4D0-C4346BC78A40.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/342FF2B2-136A-E611-AEEE-441EA158FEFE.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/3472D380-176A-E611-BE4F-A0000420FE80.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/34ADBDFF-136A-E611-9CC7-002481CFD184.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/34B0F72A-066A-E611-AB60-008CFAF74780.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/360C12D1-0F6A-E611-9F82-001E675A659A.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/36112D98-0F6A-E611-AD89-001EC9ADC294.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/36202124-306A-E611-8840-0CC47A4D7662.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/363D8882-0C6A-E611-A2C4-7CD30AB5BBBE.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/3646FFCA-166A-E611-BA4A-A0369F7F9324.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/365D0FD2-1A6A-E611-B0C3-0002C94DBB20.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/3668E1B4-056A-E611-A89C-0CC47A6C1060.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/3672E58E-0E6A-E611-A3AA-6CC2173C9150.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/36AD1056-FF69-E611-94BD-002590200850.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/36B10707-FE69-E611-A026-FA163E969C72.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/36D3FEAF-E669-E611-85D1-0002C94CD11A.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/36F21902-0A6A-E611-A625-A0369F6369D2.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/380269A6-FF69-E611-92CE-10983627C3CE.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/38160B19-0E6A-E611-8D78-6CC2173C9150.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/38408246-126A-E611-8813-A0369F7FE9FC.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/384B1949-FA69-E611-BAB5-001E67A4055F.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/38749C1F-136A-E611-93FD-002481CFE5C4.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/389B4AE2-166A-E611-BB8B-0002C94D4656.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/38CAC113-126A-E611-A881-9CB654AEBE22.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/38CE2D1A-146A-E611-95E7-002590FD0F3E.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/38DA31C7-106A-E611-A5ED-E41D2D08DCC0.root',
            '/store/mc/RunIISummer15wmLHEGS/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/100000/38E08C94-0F6A-E611-B161-001E67F8FA38.root'
            ]
    elif tag=='TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8':
        samples=['/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/00072BA3-D756-E611-8906-0CC47A4C8EBA.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/00803378-D656-E611-B44F-0CC47A4D7618.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/00937D9F-D956-E611-A753-002618FDA207.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/00C905A4-D556-E611-96AE-0CC47A74527A.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/00D31CD3-F955-E611-AB1E-50E549336064.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/02302436-D556-E611-A6C0-0CC47A4D76B8.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/02D4E065-D656-E611-9945-0025905A60BC.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/043B9B13-D856-E611-9901-0CC47A4D7658.root',
                '/store/mc/RunIISummer15GS/TTTo2L2Nu_noSC_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM/MCRUN2_71_V1-v1/20000/04553CBD-4255-E611-87DA-D4AE526A0A60.root'
                ]
    elif tag=='TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':
        samples=[
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/00025B46-CE5B-E511-A454-00215AA9D8C0.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/000B2129-F35C-E511-AF98-003048F0E1C0.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/000F5A15-E85C-E511-9A47-003048D15D48.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/00182C85-4E5B-E511-8BD8-003048D15E0E.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/0022E398-4C5B-E511-B49F-003048FFCB9E.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/0046B3BF-DF5C-E511-9A43-003048F2E8C2.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/005D2F09-305D-E511-8264-00261894385A.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/00644A9D-D95C-E511-B261-0025905A6080.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/00A96DE6-045D-E511-B21A-002590A80D9C.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/00B5712B-285D-E511-B2DD-0025905A60A6.root',
            '/store/mc/RunIISummer15GS/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/00E3D71B-E55C-E511-876B-002590AC4C72.root'
            ]
        
    return samples
