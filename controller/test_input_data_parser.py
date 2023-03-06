import pandas as pd
from .input_data_parser import parse_input_data

def test_parse_input_data():
    # input_data = "['I:MOTOR C 2 -3\n', '1633\n', '0\n', '2\n', '2\n', '2\n', '48\n', '49\n', '51\n', '116\n', '93\n', '0\n', '35\n', '992\n', '-52\n', '1\n', '0\n', '0\n', '0\n', '0\n', '88\n', '84\n', '0\n', '2353\n', '0\n', '2\n', '2\n', '2\n', '46\n', '48\n', '49\n', '111\n', '93\n', '72\n', '11\n', '987\n', '-52\n', '2\n', '-2\n', '0\n', '0\n', '0\n', '88\n', '79\n', '0\n', 'I:MOTOR A 11 -14\n', '4657\n', '1\n', '0\n', '0\n', '2\n', '48\n', '49\n', '51\n', '114\n', '93\n', '42\n', '-29\n', '990\n', '-55\n', '1\n', '0\n', '-1\n', '-1\n', '3\n', '42\n', '62\n', '0\n', 'I:MOTOR C 2 5\n', '6773\n', '1\n', '2\n', '2\n', '2\n', '46\n', '48\n', '49\n', '111\n', '94\n', '-1\n', '21\n', '995\n', '-55\n', '1\n', '0\n', '0\n', '0\n', '0\n', '22\n', '60\n', '0\n', '7441\n', '1\n', '2\n', '2\n', '1\n', '46\n', '48\n', '49\n', '111\n', '94\n', '-32\n', '20\n', '991\n', '-55\n', '1\n', '0\n', '0\n', '0\n', '0\n', '22\n', '62\n', '0\n', 'I:MOTOR C 17 -11\n', '9365\n', '0\n', '2\n', '2\n', '2\n', '50\n', '54\n', '55\n', '121\n', '95\n', '13\n', '21\n', '994\n', '-53\n', '1\n', '0\n', '0\n', '0\n', '-10\n', '22\n', '37\n', '0\n', 'I:MOTOR C 7 -11\n', '11569\n', '0\n', '1\n', '2\n', '2\n', '35\n', '36\n', '37\n', '84\n', '97\n', '0\n', '26\n', '995\n', '-48\n', '1\n', '0\n', '0\n', '0\n', '0\n', '22\n', '358\n', '0\n', '12246\n', '1\n', '0\n', '0\n', '1\n', '48\n', '51\n', '53\n', '117\n', '100\n', '-10\n', '17\n', '1015\n', '-43\n', '1\n', '0\n', '0\n', '0\n', '-11\n', '22\n', '305\n', '0\n', 'I:MOTOR A 17 10\n', '13153\n', '0\n', '1\n', '2\n', '1\n', '55\n', '58\n', '59\n', '132\n', 'None\n', '-1\n', '17\n', '1003\n', '-40\n', '1\n', '0\n', '1\n', '0\n', '-2\n', '37\n', '284\n', '0\n', 'I:MOTOR C 9 -9\n', '13829\n', '0\n', '1\n', '2\n', '1\n', '40\n', '43\n', '43\n', '97\n', '102\n', '-5\n', '31\n', '996\n', '-39\n', '1\n', '0\n', '0\n', '0\n', '0\n', '49\n', '283\n', '0\n', '14117\n', '0\n', '1\n', '2\n', '1\n', '39\n', '41\n', '43\n', '95\n', '102\n', '-4\n', '33\n', '998\n', '-39\n', '2\n', '0\n', '0\n', '0\n', '0\n', '49\n', '283\n', '0\n', '14406\n', '1\n', '1\n', '2\n', '1\n', '33\n', '35\n', '37\n', '81\n', 'None\n', '27\n', '19\n', '1001\n', '-37\n', '1\n', '-1\n', '-2\n', '0\n', '-17\n', '49\n', '265\n', '0\n', 'I:MOTOR C 20 0\n', 'I:MOTOR C 6 11\n', '15505\n', '1\n', '0\n', '0\n', '1\n', '43\n', '44\n', '47\n', '103\n', '105\n', '-3\n', '30\n', '998\n', '-33\n', '1\n', '0\n', '0\n', '0\n', '0\n', '49\n', '238\n', '0\n', '15989\n', '1\n', '0\n', '0\n', '1\n', '37\n', '39\n', '41\n', '89\n', 'None\n', '-24\n', '24\n', '993\n', '-35\n', '1\n', '1\n', '-1\n', '0\n', '7\n', '49\n', '257\n', '0\n', 'I:MOTOR A 12 -4\n', '18193\n', '0\n', '0\n', '0\n', '1\n', '45\n', '47\n', '49\n', '109\n', '103\n', '-11\n', '19\n', '1000\n', '-39\n', '1\n', '0\n', '-1\n', '0\n', '0\n', '18\n', '280\n', '0\n', 'I:MOTOR C 7 13\n', '20401\n', '0\n', '0\n', '0\n', '1\n', '44\n', '47\n', '49\n', '108\n', '103\n', '7\n', '14\n', '996\n', '-39\n', '1\n', '0\n', '-1\n', '0\n', '0\n', '15\n', '285\n', '0\n', '21173\n', '1\n', '0\n', '0\n', '1\n', '57\n', '62\n', '63\n', '139\n', 'None\n', '-17\n', '9\n', '997\n', '-42\n', '0\n', '0\n', '0\n', '0\n', '5\n', '14\n', '323\n', '0\n', 'I:MOTOR C 18 -11\n', '22453\n', '1\n', '0\n', '0\n', '2\n', '59\n', '62\n', '63\n', '142\n', '100\n', '33\n', '25\n', '1017\n', '-45\n', '0\n', '0\n', '2\n', '0\n', '-1\n', '14\n', '342\n', '0\n', 'I:MOTOR C 0 -13\n', '23281\n', '1\n', '0\n', '0\n', '2\n', '52\n', '55\n', '57\n', '125\n', '101\n', '-7\n', '13\n', '998\n', '-44\n', '0\n', '0\n', '0\n', '0\n', '0\n', '15\n', '328\n', '0\n'] "

    input_data = """I:MOTOR C 25 720
5
2
1
2
4
0
2
0
1
None
-27
67
-997
34
3
178
0
0
0
85
207
0
I:MOTOR A 25 -10
6
1
1
0
3
0
0
0
1
None
-28
70
-997
34
3
178
0
0
0
85
220
0
140
1
1
0
4
0
2
0
1
None
-27
69
-996
34
3
178
0
0
0
85
220
0
I:WAIT 1
    """

    expected_result = [
        {
            'instruction': 'I:MOTOR C 25 720',
            'measurements': [
                {
                    'time': "5",
                    'front_r': "2",
                    'front_g': "1",
                    'front_b': "2",
                    'front_intensity': "4",
                    'rear_r': "0",
                    'rear_g': "2",
                    'rear_b': "0",
                    'rear_intensity': "1",
                    'distance_sensor': "None",
                    'accelerometer_x': "-27",
                    'accelerometer_y': "67",
                    'accelerometer_z': "-997",
                    'yaw': "34",
                    'pitch': "3",
                    'roll': "178",
                    'gyro_x': "0",
                    'gyro_y': "0",
                    'gyro_z': "0",
                    'steering_motor_position': "85",
                    'driving_motor_position': "207",
                    'force_sensor_newton': "0",
                }
            ]
        },
        {
            'instruction': 'I:MOTOR A 25 -10',
            'measurements': [
                {
                    'time': '6',
                    'front_r': '1',
                    'front_g': '1',
                    'front_b': '0',
                    'front_intensity': '3',
                    'rear_r': '0',
                    'rear_g': '0',
                    'rear_b': '0',
                    'rear_intensity': '1',
                    'distance_sensor': 'None',
                    'accelerometer_x': '-28',
                    'accelerometer_y': '70',
                    'accelerometer_z': '-997',
                    'yaw': '34',
                    'pitch': '3',
                    'roll': '178',
                    'gyro_x': '0',
                    'gyro_y': '0',
                    'gyro_z': '0',
                    'steering_motor_position': '85',
                    'driving_motor_position': '220',
                    'force_sensor_newton': '0',
                },
                {
                    'time': '140',
                    'front_r': '1',
                    'front_g': '1',
                    'front_b': '0',
                    'front_intensity': '4',
                    'rear_r': '0',
                    'rear_g': '2',
                    'rear_b': '0',
                    'rear_intensity': '1',
                    'distance_sensor': 'None',
                    'accelerometer_x': '-27',
                    'accelerometer_y': '69',
                    'accelerometer_z': '-996',
                    'yaw': '34',
                    'pitch': '3',
                    'roll': '178',
                    'gyro_x': '0',
                    'gyro_y': '0',
                    'gyro_z': '0',
                    'steering_motor_position': '85',
                    'driving_motor_position': '220',
                    'force_sensor_newton': '0',
                }
            ]
        },
        {
            'instruction': "I:WAIT 1",
            'measurements': [],
        }
    ]
    
    actual_result = parse_input_data(input_data)

    assert actual_result == expected_result
