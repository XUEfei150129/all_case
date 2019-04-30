*** Settings ***
Library    case_lib.api_case_lib.LGT.Car_Basc_Info


*** Test Cases ***
验证获取车辆基本信息 -- LGT0001000
        test_getIndexMenuAndButton


验证新增/删除车辆信息 -- LGT0001001
        test_addDeleteTruck


验证修改车辆信息-- LGT0001002
        test_updateTruck


验证查询车辆信息-- LGT0001003
        test_SearchTruck



