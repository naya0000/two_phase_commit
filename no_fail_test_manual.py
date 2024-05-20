import grpc
import worker
import coordinator
import persistent_log

import twophase_pb2
import twophase_pb2_grpc

import test_util

def manual_test_set_one_value(num_workers):
    # 手動測試設置單個值的功能

    # 開始協調器和工作程序
    coordinator, workers = start_coordinator_and_workers(num_workers)
    
    # 執行設置值操作
    do_set_value('ValueA')
    
    # 檢查值是否設置正確
    check_values('ValueA')
    
    # 關閉協調器和工作程序
    shutdown_coordinator_and_workers(coordinator, workers)

    print("Manual test for setting one value with {} workers completed.".format(num_workers))

def manual_test_change_values(num_workers):
    # 手動測試更改值的功能

    # 開始協調器和工作程序
    coordinator, workers = start_coordinator_and_workers(num_workers)
    
    # 執行多個設置值操作
    do_set_value('ValueA')
    do_set_value('ValueB')
    do_set_value('ValueC')
    do_set_value('ValueD')
    do_set_value('ValueE')
    
    # 檢查值是否設置正確
    check_values('ValueE')
    
    # 關閉協調器和工作程序
    shutdown_coordinator_and_workers(coordinator, workers)

    print("Manual test for changing values with {} workers completed.".format(num_workers))

def manual_test_change_values_with_consistent_transitions(num_workers):
    # 手動測試具有一致過渡的值更改功能

    # 開始協調器和工作程序
    coordinator, workers = start_coordinator_and_workers(num_workers)
    
    # 執行具有一致過渡的多個設置值操作
    do_set_value('ValueA')
    do_set_value('ValueB', expect_transition_from='ValueA')
    do_set_value('ValueC', expect_transition_from='ValueB')
    do_set_value('ValueD', expect_transition_from='ValueC')
    do_set_value('ValueE', expect_transition_from='ValueD')
    
    # 檢查值是否設置正確
    check_values('ValueE')
    
    # 關閉協調器和工作程序
    shutdown_coordinator_and_workers(coordinator, workers)

    print("Manual test for changing values with consistent transitions with {} workers completed.".format(num_workers))

if __name__ == '__main__':
    # 手動執行各種測試
    manual_test_set_one_value(1)
    manual_test_set_one_value(2)
    manual_test_set_one_value(3)
    manual_test_set_one_value(4)
    manual_test_set_one_value(5)
    
    manual_test_change_values(1)
    manual_test_change_values(2)
    manual_test_change_values(3)
    manual_test_change_values(4)
    manual_test_change_values(5)
    
    manual_test_change_values_with_consistent_transitions(1)
    manual_test_change_values_with_consistent_transitions(2)
    manual_test_change_values_with_consistent_transitions(3)
    manual_test_change_values_with_consistent_transitions(4)
    manual_test_change_values_with_consistent_transitions(5)
