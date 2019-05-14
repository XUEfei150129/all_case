*** Settings ***
Library    case_lib.api_case_lib.DMS.Dms_Pc

*** Test Cases ***
设备生命周期管理下拉框 -- DMS0001000
        test_SysDictList


获取部门信息 -- DMS0001001
        test_GetServiceDynamicDepartInfo

设备列表-- DMS0001002
        test_SerDevLifelist

设备信息-- DMS0001003
        test_DevInfo

进退场列表-- DMS0001004
        test_SerDevEnterAndExitList

报警故障列表-- DMS0001005
        test_AlarmFaultList

订单列表-- DMS0001006
        test_Devorder_List