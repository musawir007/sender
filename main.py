import requests
from faker import Faker
from datetime import datetime
import os
import csv
os.system('clear')
print('''                                    _      
 _ __ ___  _   _ ___  __ ___      _(_)_ __
| '_ ` _ \| | | / __|/ _` \ \ /\ / / | '__|
| | | | | | |_| \__ \ (_| |\ V  V /| | |
|_| |_| |_|\__,_|___/\__,_| \_/\_/ |_|_|
''')
print('\n\n')
while True:
    fake = Faker()

    # Generate a fake first name
    first_name = fake.first_name()

    # Generate a fake last name
    last_name = fake.last_name()

    # Generate a fake Pakistani mobile number
    def generate_pakistani_phone_number():
        return f"9234{fake.random_number(digits=8, fix_len=True)}"

    phone_number = generate_pakistani_phone_number()

    # Generate a fake date of birth for someone aged 18 or older
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=27)
    formatted_date_of_birth = date_of_birth.strftime('%d-%m-%Y')



    f_name =first_name

    full =f"{first_name} {last_name}"

    full_name = full

    last_name = last_name

    number = phone_number




    # print(f"First Name: {first_name}")
    # print(f"Last Name: {last_name}")
    # print(f"Mobile Number: {'+'}{phone_number}")
    # print(f"Date of Birth: {formatted_date_of_birth}")

    cookies = {
        'sb': '5yyxZgFzfpzpwIL3SPOfxW_k',
        'datr': '5yyxZixz_qEXAZ3WPuxBviQX',
        'locale': 'en_GB',
        'ps_l': '1',
        'ps_n': '1',
        'dpr': '2',
        'm_pixel_ratio': '2',
        'wd': '400x63',
        'rs': f'04%7C03%7C2000%7C%7C%2B{number}%7C{f_name}%7C{last_name}%7C{f_name}+{last_name}',
        'fr': '0Tix7l8XavJXcLEdT.AWVmATskY1zCenMpoi-8SGW6Nhs.BmsSzn..AAA.0.0.BmsS_a.AWV7pGgxFxQ',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        
        'origin': 'https://m.facebook.com',
        'priority': 'u=1, i',
        'referer': 'https://m.facebook.com/reg/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.89", "Chromium";v="127.0.6533.89"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"Nexus 5"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"6.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'appid': 'com.bloks.www.bloks.caa.reg.create.account.async',
        'type': 'action',
        '__bkv': '24a21656ef71e2be6a9ee56bf83edca824e9093432f3ee09230a0c20f935e159',
    }





    data = {
        '__aaid': '0',
        '__user': '0',
        '__a': '1',
        '__req': 'v',
        '__hs': '19940.BP:wbloks_caa_pkg.2.0..0.0',
        'dpr': '3',
        '__ccg': 'GOOD',
        '__rev': '1015407831',
        '__s': ':ugs3zb:4demdp',
        '__hsi': '7399747878569706749',
        '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09Mx60se2G0pS0ny0oi0zE5W0PU881eEdEG0xo2ewbS1LwpEcE1kU1bo8Xwn98aU3jw',
        '__csr': '',
        'fb_dtsg': 'NAcMgtsaTtUUM_r0X9c1pxS9YWwRPUH9lFXsKnt2UW-a992qdQrjPEg:0:0',
        'jazoest': '24978',
        'lsd': 'AVo2uMELfPI',
        'params': '{"params":"{\\"server_params\\":{\\"event_request_id\\":\\"98f21bc3-a61c-457f-b7ec-67d3479d2601\\",\\"app_id\\":0,\\"reg_info\\":\\"{\\\\\\"first_name\\\\\\":\\\\\\"'+f_name+'\\\\\\",\\\\\\"last_name\\\\\\":\\\\\\"'+last_name+'\\\\\\",\\\\\\"full_name\\\\\\":\\\\\\"'+full_name+'\\\\\\",\\\\\\"contactpoint\\\\\\":\\\\\\"+'+number+'\\\\\\",\\\\\\"ar_contactpoint\\\\\\":null,\\\\\\"contactpoint_type\\\\\\":\\\\\\"phone\\\\\\",\\\\\\"is_using_unified_cp\\\\\\":false,\\\\\\"unified_cp_screen_variant\\\\\\":null,\\\\\\"is_cp_auto_confirmed\\\\\\":false,\\\\\\"is_cp_auto_confirmable\\\\\\":false,\\\\\\"confirmation_code\\\\\\":null,\\\\\\"birthday\\\\\\":\\\\\\"'+formatted_date_of_birth+'\\\\\\",\\\\\\"did_use_age\\\\\\":false,\\\\\\"gender\\\\\\":1,\\\\\\"use_custom_gender\\\\\\":false,\\\\\\"custom_gender\\\\\\":null,\\\\\\"encrypted_password\\\\\\":\\\\\\"#PWD_BROWSER:5:1722888147:AcpQAJK1sVaaeYuFKTKMzk\\\\\\\\/MfSKnJ38dC2+FUuIYmUh37M99s30vPxpUrY\\\\\\\\/No+S8947KaR70D3C4Gh4jALlV0djAaWx98TxBif70ORSw4IZ+4fhiMdO\\\\\\\\/BtUJ91yfv4+2Q0k6lepDN9zjsccNaCXf\\\\\\",\\\\\\"username\\\\\\":null,\\\\\\"username_prefill\\\\\\":null,\\\\\\"fb_conf_source\\\\\\":null,\\\\\\"device_id\\\\\\":null,\\\\\\"ig4a_qe_device_id\\\\\\":null,\\\\\\"family_device_id\\\\\\":null,\\\\\\"nta_eligibility_reason\\\\\\":null,\\\\\\"ig_nta_test_group\\\\\\":null,\\\\\\"user_id\\\\\\":null,\\\\\\"safetynet_token\\\\\\":null,\\\\\\"safetynet_response\\\\\\":null,\\\\\\"machine_id\\\\\\":null,\\\\\\"profile_photo\\\\\\":null,\\\\\\"profile_photo_id\\\\\\":null,\\\\\\"profile_photo_upload_id\\\\\\":null,\\\\\\"avatar\\\\\\":null,\\\\\\"email_oauth_token_no_contact_perm\\\\\\":null,\\\\\\"email_oauth_token\\\\\\":null,\\\\\\"email_oauth_tokens\\\\\\":[],\\\\\\"should_skip_two_step_conf\\\\\\":null,\\\\\\"openid_tokens_for_testing\\\\\\":null,\\\\\\"encrypted_msisdn\\\\\\":null,\\\\\\"encrypted_msisdn_for_safetynet\\\\\\":null,\\\\\\"cached_headers_safetynet_info\\\\\\":null,\\\\\\"should_skip_headers_safetynet\\\\\\":null,\\\\\\"headers_last_infra_flow_id\\\\\\":null,\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\":null,\\\\\\"headers_flow_id\\\\\\":\\\\\\"b51cd785-a100-499a-a991-eb5433393548\\\\\\",\\\\\\"was_headers_prefill_available\\\\\\":false,\\\\\\"sso_enabled\\\\\\":null,\\\\\\"existing_accounts\\\\\\":null,\\\\\\"used_ig_birthday\\\\\\":null,\\\\\\"sync_info\\\\\\":null,\\\\\\"create_new_to_app_account\\\\\\":null,\\\\\\"skip_session_info\\\\\\":null,\\\\\\"ck_error\\\\\\":null,\\\\\\"ck_id\\\\\\":null,\\\\\\"ck_nonce\\\\\\":null,\\\\\\"should_save_password\\\\\\":false,\\\\\\"horizon_synced_username\\\\\\":null,\\\\\\"fb_access_token\\\\\\":null,\\\\\\"horizon_synced_profile_pic\\\\\\":null,\\\\\\"is_identity_synced\\\\\\":false,\\\\\\"is_msplit_reg\\\\\\":null,\\\\\\"user_id_of_msplit_creator\\\\\\":null,\\\\\\"dma_data_combination_consent_given\\\\\\":null,\\\\\\"xapp_accounts\\\\\\":null,\\\\\\"fb_device_id\\\\\\":null,\\\\\\"fb_machine_id\\\\\\":null,\\\\\\"ig_device_id\\\\\\":null,\\\\\\"ig_machine_id\\\\\\":null,\\\\\\"should_skip_nta_upsell\\\\\\":null,\\\\\\"big_blue_token\\\\\\":null,\\\\\\"skip_sync_step_nta\\\\\\":null,\\\\\\"caa_reg_flow_source\\\\\\":\\\\\\"login_home_native_integration_point\\\\\\",\\\\\\"ig_authorization_token\\\\\\":null,\\\\\\"full_sheet_flow\\\\\\":false,\\\\\\"crypted_user_id\\\\\\":null,\\\\\\"is_caa_perf_enabled\\\\\\":false,\\\\\\"is_preform\\\\\\":true,\\\\\\"ignore_suma_check\\\\\\":false,\\\\\\"ignore_existing_login\\\\\\":false,\\\\\\"ignore_existing_login_from_suma\\\\\\":false,\\\\\\"ignore_existing_login_after_errors\\\\\\":false,\\\\\\"suggested_first_name\\\\\\":null,\\\\\\"suggested_last_name\\\\\\":null,\\\\\\"suggested_full_name\\\\\\":null,\\\\\\"frl_authorization_token\\\\\\":null,\\\\\\"post_form_errors\\\\\\":null,\\\\\\"skip_step_without_errors\\\\\\":false,\\\\\\"existing_account_exact_match_checked\\\\\\":false,\\\\\\"existing_account_fuzzy_match_checked\\\\\\":false,\\\\\\"confirmation_code_send_error\\\\\\":null,\\\\\\"is_too_young\\\\\\":false,\\\\\\"source_account_type\\\\\\":null,\\\\\\"whatsapp_installed_on_client\\\\\\":false,\\\\\\"confirmation_medium\\\\\\":null,\\\\\\"source_credentials_type\\\\\\":null,\\\\\\"source_cuid\\\\\\":null,\\\\\\"source_account_reg_info\\\\\\":null,\\\\\\"soap_creation_source\\\\\\":null,\\\\\\"source_account_type_to_reg_info\\\\\\":null,\\\\\\"registration_flow_id\\\\\\":\\\\\\"1e15636f-ff1e-44e7-92d4-45edd5ed6412\\\\\\",\\\\\\"should_skip_youth_tos\\\\\\":false,\\\\\\"is_youth_regulation_flow_complete\\\\\\":false,\\\\\\"is_on_cold_start\\\\\\":false,\\\\\\"email_prefilled\\\\\\":false,\\\\\\"cp_confirmed_by_auto_conf\\\\\\":false,\\\\\\"auto_conf_info\\\\\\":null,\\\\\\"in_sowa_experiment\\\\\\":false,\\\\\\"youth_regulation_config\\\\\\":null,\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\":null,\\\\\\"conf_bouncing_cliff_screen_type\\\\\\":null,\\\\\\"conf_show_bouncing_cliff\\\\\\":null,\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\":false,\\\\\\"flash_call_permissions_status\\\\\\":null,\\\\\\"attestation_result\\\\\\":null,\\\\\\"request_data_and_challenge_nonce_string\\\\\\":null,\\\\\\"confirmed_cp_and_code\\\\\\":null,\\\\\\"in_updated_eu_tos\\\\\\":false,\\\\\\"notification_callback_id\\\\\\":null,\\\\\\"reg_suma_state\\\\\\":0,\\\\\\"is_msplit_neutral_choice\\\\\\":false,\\\\\\"zero_tap_enabled\\\\\\":false,\\\\\\"msg_previous_cp\\\\\\":null,\\\\\\"ntp_import_source_info\\\\\\":null,\\\\\\"youth_consent_decision_time\\\\\\":null,\\\\\\"username_screen_experience\\\\\\":\\\\\\"control\\\\\\",\\\\\\"reduced_tos_test_group\\\\\\":\\\\\\"control\\\\\\",\\\\\\"should_show_spi_before_conf\\\\\\":true,\\\\\\"google_oauth_account\\\\\\":null,\\\\\\"is_reg_request_from_ig_suma\\\\\\":false,\\\\\\"is_igios_spc_reg\\\\\\":false,\\\\\\"device_emails\\\\\\":[],\\\\\\"is_toa_reg\\\\\\":false,\\\\\\"is_threads_public\\\\\\":false,\\\\\\"spc_import_flow\\\\\\":false}\\",\\"flow_info\\":\\"{\\\\\\"flow_name\\\\\\":\\\\\\"new_to_family_fb_default\\\\\\",\\\\\\"flow_type\\\\\\":\\\\\\"ntf\\\\\\"}\\",\\"current_step\\":9,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"91445345000040\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"cc24e4b8-907f-427a-be64-00e5824d9d22\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"F2_FLOW\\",\\"INTERNAL_INFRA_THEME\\":\\"harm_f\\"},\\"client_input_params\\":{\\"device_id\\":\\"\\",\\"waterfall_id\\":\\"cc24e4b8-907f-427a-be64-00e5824d9d22\\",\\"machine_id\\":\\"\\",\\"ck_error\\":\\"\\",\\"ck_id\\":\\"\\",\\"ck_nonce\\":\\"\\",\\"should_ignore_existing_login\\":0,\\"encrypted_msisdn\\":\\"\\",\\"headers_last_infra_flow_id\\":\\"\\",\\"reached_from_tos_screen\\":1,\\"no_contact_perm_email_oauth_token\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\",\\"lara_override\\":\\"\\"}}}"}',
    }

    response = requests.post('https://m.facebook.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

    print(response.status_code)

    cok = response.cookies.get_dict()

    # print(f"\ncookies: {cok}")
    # print(f"\nuid: {cok['c_user']}")

    rsp = requests.get('https://m.facebook.com/confirmemail.php', params=params, cookies=cok, headers=headers)

    print(rsp.status_code)
    # print(rsp.url)
    nm = f"{'+'}{number}"
    if "https://m.facebook.com/conf/notifmedium/?" in rsp.url:
        print(f"Number: {'+'}{phone_number} uid: {cok['c_user']} pass: musawirabro")
        print('\nworking')
        with open("working.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name,nm,cok['c_user'],'musawirabro'])
    else:
        print("not create id")
