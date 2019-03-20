*** Settings ***
Library    case_lib.api_case_lib.logistics.Car_Basc_Info


*** Test Cases ***
验证获取车辆基本信息 -- tc001000
        test_getIndexMenuAndButton


验证新增车辆信息 -- tc001002
        test_addDeleteTruck


验证修改车辆信息-- tc001003
        test_updateTruck