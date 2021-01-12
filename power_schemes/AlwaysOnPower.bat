@echo off



::------------------------------------------------
::
::  THIS SCRIPT CREATES AN ALWAYS ON POWER SCHEME
::
::  Batch file actions
::   1) Find the active scheme
::   2) Duplicate the active scheme
::   3) Rename the new scheme
::   4) Change settings of the newly created scheme
::   5) Make the new scheme active
::
::------------------------------------------------


::Step 1: Find the active scheme

    for /f "tokens=2 delims=:(" %%x in ('powercfg -getactivescheme') do set ActiveSchemeGUID=%%x

	

::Step 2: Duplicate the active scheme

    for /f "tokens=2 delims=:(" %%y in ('powercfg -duplicatescheme %ActiveSchemeGUID%') do set NewSchemeGUID=%%y


	
::Step 3: Rename the new scheme "AlwaysOn"

    powercfg -changename %NewSchemeGUID% AlwaysOn "Always on power scheme"
 

 
::Step 4: Change settings of the newly created scheme

  ::Subgroup GUID: fea3413e-7e05-4911-9a71-700331f1c294  (Settings belonging to no subgroup)
    ::Power Setting GUID: 0e796bdb-100d-47d6-a2d5-f7d2daa51f51  (Require a password on wakeup)
      ::Possible Setting Index: 000
      ::Possible Setting Friendly Name: No
      ::Possible Setting Index: 001
      ::Possible Setting Friendly Name: Yes
    ::Current AC Power Setting Index: 0x00000001
    ::Current DC Power Setting Index: 0x00000001
   powercfg /setacvalueindex %NewSchemeGUID% fea3413e-7e05-4911-9a71-700331f1c294 0e796bdb-100d-47d6-a2d5-f7d2daa51f51 000
   powercfg /setdcvalueindex %NewSchemeGUID% fea3413e-7e05-4911-9a71-700331f1c294 0e796bdb-100d-47d6-a2d5-f7d2daa51f51 000

  ::Subgroup GUID: 0012ee47-9041-4b5d-9b77-535fba8b1442  (Hard disk)
    ::Power Setting GUID: 6738e2c4-e8a5-4a42-b16a-e040e769756e  (Turn off hard disk after)
      ::Minimum Possible Setting: 0x00000000
      ::Maximum Possible Setting: 0xffffffff
      ::Possible Settings increment: 0x00000001
      ::Possible Settings units: Seconds
    ::Current AC Power Setting Index: 0x000004b0
    ::Current DC Power Setting Index: 0x00000258
   powercfg /setacvalueindex %NewSchemeGUID% 0012ee47-9041-4b5d-9b77-535fba8b1442 6738e2c4-e8a5-4a42-b16a-e040e769756e 000
   powercfg /setdcvalueindex %NewSchemeGUID% 0012ee47-9041-4b5d-9b77-535fba8b1442 6738e2c4-e8a5-4a42-b16a-e040e769756e 000

  ::Subgroup GUID: 238c9fa8-0aad-41ed-83f4-97be242c8f20  (Sleep)
    ::Power Setting GUID: 29f6c1db-86da-48c5-9fdb-f2b67b1f44da  (Sleep after)
      ::Minimum Possible Setting: 0x00000000
      ::Maximum Possible Setting: 0xffffffff
      ::Possible Settings increment: 0x00000001
      ::Possible Settings units: Seconds
    ::Current AC Power Setting Index: 0x00000708
    ::Current DC Power Setting Index: 0x00000384
   powercfg /setacvalueindex %NewSchemeGUID% 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 000
   powercfg /setdcvalueindex %NewSchemeGUID% 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 000

    ::Power Setting GUID: 9d7815a6-7ee4-497e-8888-515a05f02364  (Hibernate after)
      ::Minimum Possible Setting: 0x00000000
      ::Maximum Possible Setting: 0xffffffff
      ::Possible Settings increment: 0x00000001
      ::Possible Settings units: Seconds
    ::Current AC Power Setting Index: 0x00005460
    ::Current DC Power Setting Index: 0x00005460
   powercfg /setacvalueindex %NewSchemeGUID% 238c9fa8-0aad-41ed-83f4-97be242c8f20 9d7815a6-7ee4-497e-8888-515a05f02364 000
   powercfg /setdcvalueindex %NewSchemeGUID% 238c9fa8-0aad-41ed-83f4-97be242c8f20 9d7815a6-7ee4-497e-8888-515a05f02364 000

   ::Subgroup GUID: 2a737441-1930-4402-8d77-b2bebba308a3  (USB settings)
    ::Power Setting GUID: 48e6b7a6-50f5-4782-a5d4-53bb8f07e226  (USB selective suspend setting)
      ::Possible Setting Index: 000
      ::Possible Setting Friendly Name: Disabled
      ::Possible Setting Index: 001
      ::Possible Setting Friendly Name: Enabled
    ::Current AC Power Setting Index: 0x00000001
    ::Current DC Power Setting Index: 0x00000001
   powercfg /setacvalueindex %NewSchemeGUID% 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 000
   powercfg /setdcvalueindex %NewSchemeGUID% 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 000
   
  ::Subgroup GUID: 4f971e89-eebd-4455-a8de-9e59040e7347  (Power buttons and lid)
    ::Power Setting GUID: 5ca83367-6e45-459f-a27b-476b1d01c936  (Lid close action)
      ::Possible Setting Index: 000
      ::Possible Setting Friendly Name: Do nothing
      ::Possible Setting Index: 001
      ::Possible Setting Friendly Name: Sleep
      ::Possible Setting Index: 002
      ::Possible Setting Friendly Name: Hibernate
      ::Possible Setting Index: 003
      ::Possible Setting Friendly Name: Shut down
    ::Current AC Power Setting Index: 0x00000000
    ::Current DC Power Setting Index: 0x00000000
   powercfg /setacvalueindex %NewSchemeGUID% 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 000
   powercfg /setdcvalueindex %NewSchemeGUID% 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 000


::Step 5: Make the new scheme active

   powercfg -setactive %NewSchemeGUID%