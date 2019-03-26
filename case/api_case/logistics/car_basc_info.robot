*** Settings ***
Library    case_lib.api_case_lib.logistics.Car_Basc_Info


*** Test Cases ***
验证获取车辆基本信息 -- wl001000
        test_getIndexMenuAndButton


验证新增/删除车辆信息 -- wl001001
        test_addDeleteTruck


验证修改车辆信息-- wl001002
        test_updateTruck


验证查询车辆信息-- wl001003
        test_SearchTruck