# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:54:52 2019

@author: antonc3
"""

# import xml.etree.ElementTree as ET
import os
import sys
import webbrowser as wb
import re
import webbrowser as wb
from lxml import etree as ET


# All predefined meta varaiables defined in table-map.xml
tag_seen = []
table_map_metas = ['device.class', 'device.ip', 'device.ipv6', 'device.type', 'device.type.id', 'device.host',
                   'event_cat', 'event_cat_name', 'event.cat', 'event.cat.name', 'forward.ip', 'forward.ipv6',
                   'header.id', 'level', 'msg_id', 'parse.error', 'vid', 'lc.cid', 'lc.ctime', 'device.group',
                   'access_point', 'accesses', 'action', 'administrator', 'agent', 'application', 'audit_class',
                   'authmethod', 'bcc', 'binary', 'bssid', 'bytes', 'c_domain', 'sdomain', 'c_username', 'c_sid',
                   'calling_from', 'calling_to', 'category', 'cc', 'cert_error', 'cert_hostname', 'cert_hostname_cat',
                   'cert_status', 'cert_subject', 'cert_ca', 'cert_checksum',  'change_attribute', 'change_new', 'change_old', 'checksum',
                   'child_pid', 'child_pid_val', 'child_process', 'comments', 'component_version', 'connectionid',
                   'content_type', 'content_version', 'context', 'cpu', 'cve', 'd_cipher', 'd_ciphersize', 'd_sslver',
                   'daddr', 'daddr_v6', 'data', 'db_id', 'db_name', 'db_pid', 'dclass_counter1',
                   'dclass_counter1_string', 'dclass_counter2', 'dclass_counter2_string', 'dclass_counter3',
                   'dclass_counter3_string', 'dclass_ratio1', 'dclass_ratio1_string', 'dclass_ratio2',
                   'dclass_ratio2_string', 'dclass_ratio3', 'dclass_ratio3_string', 'ddomain', 'dead', 'device',
                   'devicehostname', 'detail', 'dhost', 'dinterface', 'direction', 'directory', 'disk_volume',
                   'disposition', 'dmacaddr', 'dmask', 'dn', 'doc_number', 'domain', 'domain_id', 'domainname', 'dport',
                   'dst_dn', 'dst_payload', 'dst_spi', 'dst_zone', 'dtransaddr', 'dtransport', 'duration',
                   'duration_string', 'ec_activity', 'ec_outcome', 'ec_subject', 'ec_theme', 'effective_time',
                   'encryption_type', 'endtime', 'entry', 'event_computer', 'event_counter', 'event_description',
                   'event_log', 'event_queue_time', 'event_source', 'event_state', 'event_time', 'event_time_string',
                   'event_type', 'event_name', 'event_user', 'expected_val', 'expiration_time',
                   'expiration_time_string', 'fcatnum', 'federated_idp', 'federated_sp', 'filename', 'filename_size',
                   'filetype', 'filter', 'fqdn', 'fresult', 'from', 'gateway', 'group', 'group_object', 'groupid',
                   'h_code', 'hardware_id', 'hostid', 'hostip', 'hostip_v6', 'hostname', 'icmpcode', 'icmptype', 'id',
                   'id1', 'id2', 'ike', 'ike_cookie1', 'ike_cookie2', 'index', 'info', 'inode', 'instance', 'interface',
                   'ip_proto', 'jobnum', 'library', 'listnum', 'location_city', 'location_country', 'location_desc',
                   'location_dst', 'location_src', 'location_state', 'logon_id', 'logon_type', 'lread', 'lun', 'lwrite',
                   'macaddr', 'mail_id', 'mask', 'message_body', 'msg', 'network_port', 'network_service', 'node',
                   'nodename', 'obj_id', 'obj_name', 'obj_server', 'obj_type', 'obj_value', 'observed_val',
                   'operation_id', 'orig_ip', 'os', 'owner', 'packets', 'paddr', 'param', 'parent_node', 'parent_pid',
                   'parent_pid_val', 'patient_fname', 'patient_fullname', 'patient_id', 'patient_lname',
                   'patient_mname', 'peer', 'peer_id', 'permissions', 'phone_number', 'policy_id', 'policy_value',
                   'policyname', 'pool_id', 'pool_name', 'portname', 'pread', 'privilege', 'process', 'process_id',
                   'process_id_val', 'processing_time', 'process_src', 'process_id_src', 'product', 'profile',
                   'protocol', 'protocol_detail', 'pwwn', 'r_hostid', 'rbytes', 'realm', 'recorded_time',
                   'reputation_num', 'resource', 'resource_class', 'result', 'resultcode', 'risk', 'risk_num',
                   'risk_num_comm', 'risk_num_static', 'risk_num_next', 'risk_num_sand', 'rule', 'rule_group',
                   'rule_template', 'rule_uid', 'rulename', 's_cipher', 's_ciphersize', 's_context', 's_sslver',
                   'saddr', 'saddr_v6', 'sbytes', 'scheme', 'sensor', 'serial_number', 'service', 'service_account',
                   'sessionid', 'sessionid1', 'severity', 'shost', 'sid', 'sigid', 'sigid_string', 'sigid1', 'signame',
                   'sigtype', 'sinterface', 'site', 'smacaddr', 'smask', 'sport', 'src_dn', 'src_payload', 'src_spi',
                   'src_zone', 'ssid', 'stamp', 'starttime', 'statement', 'stransaddr', 'stransport', 'subject',
                   't_context', 'tbl_name', 'tcp_flags', 'terminal', 'threat_name', 'threat_val', 'timezone', 'to',
                   'tos', 'trans_from', 'trans_id', 'trans_to', 'trigger_desc', 'trigger_val', 'uid', 'url', 'url_raw',
                   'user_address', 'user_agent', 'user_dept', 'user_fname', 'user_fullname', 'user_lname', 'user_mname',
                   'user_org', 'user_role', 'username', 'vendor_event_cat', 'version', 'virusname', 'vlan', 'vm_target',
                   'vsys', 'vuln_ref', 'web_cookie', 'web_domain', 'web_extension', 'web_host', 'web_method',
                   'web_query', 'web_ref_domain', 'web_ref_host', 'web_ref_page', 'web_ref_query', 'web_ref_root',
                   'web_referer', 'web_root', 'webpage', 'wifi_channel', 'wlan', 'workspace_desc', 'workstation',
                   'zone', 'ad_computer_dst', 'alert_id', 'attachment', 'extension', 'eth_type', 'feed_desc',
                   'feed_name', 'latdec_dst', 'latdec_src', 'longdec_src', 'org_dst', 'referer', 'risk_info',
                   'risk_suspicious', 'risk_warning', 'threat_source','space','inout','pool_member']
header_id_seen = []
message_id_seen = []


class Error_Node:
    def __init__(self, node):
        self.node = node
        self.errors_found = []


def check_all_header_attributes_present(child):
    """
    checks whether header attributes id1,id2 are present or not.
    """
    error_lists = []
    if "id1" not in child.attrib:
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + child.attrib.get('id1', 'None'),
                      'description': "ID1_NOT_PRESENT:id1 attribute not present"}
        error_lists.append(error_dict)
    if "id2" not in child.attrib:
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + child.attrib.get('id1', 'None'),
                      "description": "ID2_NOT_PRESENT:'id2' attribute not present"}
        error_lists.append(error_dict)
    if "content" not in child.attrib:
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + child.attrib.get('id1', 'None'),
                      "description": "CONTENT_ATTRIBUTE_NOT_PRESENT:'content' attribute not present"}
        error_lists.append(error_dict)
    if "content" in child.attrib and child.attrib['content'] == '':
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + child.attrib.get('id1', 'None'),
                      "description": "CONTENT_ATTRIBUTE_IS_EMPTY:'content' attr should not be empty"}
        error_lists.append(error_dict)
		
    return error_lists


def check_header_id_equality(child):
    """
    Function checks whether header id1 and id2 are equal or not"
    """
    id1 = child.attrib['id1']
    id2 = child.attrib['id2']
    error_list = []
    if id1 != id2:
        print (str(id1) + "Fatal:id1 should be equal to id2")
        # fout.write("FATAL:id1='"+str(id1)+"',id2='"+str(id2)+"'id1 should be equal to id2\n")
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + id1,
                      'description': "HEADER_ID1_ID2_NOT_EQUAL 'id1' should be equal to 'id2'"}
        error_list.append(error_dict)
    return error_list


def check_header_ids_integers_or_not(child):
    """
    Check whether id1 and id2 are integers or not.
    """
    id1 = child.attrib['id1']
    id2 = child.attrib['id2']
    error_list = []
    try:
        id1 = int(id1)
    except Exception as e:
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + str(id1),
                      'description': "HEADER_ID1_NOT_INTEGER 'id1' should be an integer value"}
        error_list.append(error_dict)
    try:
        id2 = int(id2)
    except Exception as e:
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + str(id1),
                      'description': "HEADER_ID2_NOT_INTEGER 'id2' should be an integer value"}
        error_list.append(error_dict)
    return error_list


def check_duplicate_header_id(child):
    """
    checks for duplicate headers
    """
    id1 = child.attrib['id1']
    error_dict = {}
    error_list = []
    if id1 in header_id_seen:
        error_dict = {'severity': 'FATAL', 'id1': "Header id1:" + id1,
                      'description': "DUPLICATE_HEADER_FOUND: Header id should be unique"}
        error_list.append(error_dict)
    header_id_seen.append(id1)

    return error_list


def check_messageid_tag_and_content_line_meta(child):
    """
    Function checks for messageid meta in content line if messageid attribute exists.
    """
    error_list = []
    error_dict = {}
    if "messageid" in child.attrib and child.attrib.get('messageid', None) != '' and 'content' in child.attrib:
        content = child.attrib.get("content", None)
        # print ("conntent:",content,"messageid" in content)
        if "<messageid>" in content:
            error_dict = {'severity': 'FATAL', 'id1': "Header: " + child.attrib.get('id1', 'None'),
                          'description': "MESSAGEID_META_NOT_ALLOWED: messageid meta not allowed in content line since header contains explicit messageid tag"}
            error_list.append(error_dict)
    elif "messageid" not in child.attrib and child.attrib.get('messageid', None) != '' and 'content' in child.attrib:
        content = child.attrib.get("content", None)
        # print ("conntent:",content,"messageid" in content)
        if "<messageid>" not in content:
            error_dict = {'severity': 'FATAL', 'id1': "Header: " + child.attrib.get('id1', 'None'),
                          'description': "MESSAGEID_META_NOT_PRESENT_IN_CONTENT_LINE: messageid meta should be present content line since header doen't have explicit messageid tag"}
            error_list.append(error_dict)
    return error_list


def check_all_messageid_attributes_present(child):
    """
    checks weather all mandatory attributes of messageid's are present or not
    """
    error_list = []
    attributes = ['id1','id2','eventcategory','content']
    for attribute in attributes:
        if attribute in child.attrib and child.attrib[attribute] == '':
            error_dict = {"severity": "FATAL", "id1": "Messageid: " + child.attrib.get('id1', 'None'),"description": "EMPTY_ATTRIBUTES_ARE_NOT_ALLOWED :'"+attribute+"' can not be empty"}
            error_list.append(error_dict)		  

            
    if "id1" not in child.attrib:
        error_dict = {"severity": "FATAL", "id1": "Messageid: " + child.attrib.get('id1', 'None'),
                      "description": "MESSAGE_ID1_NOT_PRESENT : messageid1 is not present"}
        error_list.append(error_dict)
    if "id2" not in child.attrib:
        error_dict = {"severity": "FATAL", "id1": "Messageid: " + child.attrib.get('id1', 'None'),
                      "description": "MESSAGE_ID2_NOT_PRESENT : messageid2 is not present"}
        error_list.append(error_dict)
    if "eventcategory" not in child.attrib:
        error_dict = {"severity": "FATAL", "id1": "Messageid: " + child.attrib.get('id1', 'None'),
                      "description": "EVENT_CATEGORY_TAG_NOT_PRESENT : eventcategory tag is not present"}
        error_list.append(error_dict)
    if "content" not in child.attrib:
        error_dict = {"severity": "FATAL", "id1": "Messageid: " + child.attrib.get('id1', 'None'),
                      "description": "CONTENT_TAG_NOT_PRESENT : content attribute not present"}
        error_list.append(error_dict)
    if "content" in child.attrib and child.attrib["content"] == '':
        error_dict = {"severity": "FATAL", "id1": "Messageid: " + child.attrib.get('id1', 'None'),
                      "description": "EMPTY_CONTENT_LINE_NOT_ALLOWED : content attribute not present"}
        error_list.append(error_dict)	  
    return error_list


def check_duplicate_message_id(child):
    """
    Checks for duplicate messageid's
    """
    id1 = child.attrib['id1']
    error_dict = {}
    error_list = []
    if id1 in message_id_seen:
        error_dict = {'severity': 'FATAL', 'id1': "Messageid:" + id1,
                      'description': "DUPLICATE_MESSAGE_ID_FOUND: Messageid should be unique"}
    message_id_seen.append(id1)
    error_list.append(error_dict)
    return error_list


def check_meta_present_in_MVG(child):
    """
    Checks whether the meta name is present in table-map.xml
    """
    error_list = []
    if "content" in child.attrib:
        content = child.attrib["content"]
        content = re.sub(r'<<\w+>', '', content)
        pat = r'<\w+>|<\w+\.\w+>|<\w+\.\w+\.\w+>'
        metas = re.findall(pat, content)
        # print ("metas",metas)
        metas = [item.replace("<", '').replace(">", '').replace("{", '').replace("}", '').strip() for item in metas]
        functions = [item.split(":")[0].strip("@") for item in metas if item.startswith("@")]
        functions = [item for item in functions if not item.startswith('fld')]
        functions = [item for item in functions if item != '']
        metas = [meta for meta in metas if meta not in functions and '@' not in meta and not meta.startswith('fld')]
        for meta in metas:
            if meta not in table_map_metas:
                error_dict = {'severity': 'ERROR', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                              'description': "VARIABLE_NAME_NOT_ALLOWED: variable '" + meta + "' name is not present in table-map.xml and MVG"}
                error_list.append(error_dict)
        for function in functions:
            if function not in table_map_metas:
                error_dict = {'severity': 'ERROR', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                              'description': "VARIABLE_NAME_NOT_ALLOWED: variable '" + function + "' name is not present in table-map.xml and MVG"}
                error_list.append(error_dict)

    if "functions" in child.attrib:
        """ check whether the function meta is present in table-map.xml"""
        if "functions" in child.attrib:
            functions = child.attrib["functions"]
            pat = r"<.*?>"
            functions = re.findall(pat, functions)
            functions = [item.lstrip("<").rstrip(">") for item in functions]
            functions = [item.split(":")[0].strip("@") for item in functions if item.startswith("@")]
            functions = L = [item for item in functions if item != '']
            for function in functions:
                #print (function)
                if function.strip() not in table_map_metas and not function.strip().startswith('fld'):
                    error_dict = {'severity': 'ERROR', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "VARIABLE_NAME_NOT_ALLOWED: variable '" + function + "' name is not present in table-map.xml and MVG"}
                    error_list.append(error_dict)
    return error_list


def check_special_characters_in_messageid(child):
    """
    Function checks whether any special characters like "," or white spaces present in id1 and id2 attributes
    """
    id1 = child.attrib["id1"]
    id2 = child.attrib["id2"]
    error_list = []
    if "," in id1:
        error_dict = {'severity': 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "SPECIAL_CHARACTERS_NOT_ALLOWED_IN_ID1: ',' is not allowed in id1"}
        error_list.append(error_dict)
    if " " in id1:
        error_dict = {'severity': 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "SPECIAL_CHARACTERS_NOT_ALLOWED_IN_ID1: white space is not allowed in id1"}
        error_list.append(error_dict)
    if "," in id2:
        error_dict = {'severity': 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "SPECIAL_CHARACTERS_NOT_ALLOWED_IN_ID1: ',' is not allowed in id2"}
        error_list.append(error_dict)
    if " " in id2:
        error_dict = {'severity': 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "SPECIAL_CHARACTERS_NOT_ALLOWED_IN_ID1: white space is not allowed in id2"}
        error_list.append(error_dict)
    return error_list


def check_function_parameter_name_exists_in_metas(child):
    """
    Function checks whether function parameter exists in meta varaibles defined in content
    """
    error_list = []
    functions_dict = {}
    functions_list = []

    if "functions" in child.attrib and "content" in child.attrib:
        content = child.attrib.get("content", None)
        pat = r"<.*?>"
        metas = re.findall(pat, content)
        metas = [item.lstrip("<").rstrip(">") for item in metas]
        if "functions" in child.attrib:
            functions2 = child.attrib["functions"]
            pat = r"<.*?>"
            functions = re.findall(pat, functions2)
            function_metas = [item.split(":")[0].strip("<").strip(">").replace("@", '') for item in functions]
            # print ("function_metas",function_metas)
            metas += function_metas
            for fun in functions:
                if '*STRCAT' in fun:
                    continue
                functions_dict = {}
                if re.search(r"@\w+:\*\w+\(.*?\)", fun):
                    function_name = re.findall("\*\w+\(", fun)[0].strip("*").strip("\(")
                    function_param = function_param = re.findall(r"\(.*?\)", fun)[0]
                    function_param = function_param.strip('\(').strip('\)')
                    functions_dict['function_name'] = function_name
                    functions_dict['function_param'] = function_param
                    functions_list.append(functions_dict)
            # functions=[item for item in functions if item!='']
            # metas=[meta for meta in metas if meta not in functions and '@' not in meta and not meta.startswith('fld')]
            for fun_dict in functions_list:
                if "," in fun_dict['function_param'] and '$HDR' not in fun_dict['function_param'] and fun_dict[
                    'function_name'] != 'HDR':
                    params = fun_dict['function_param'].split(",")
                    for param in params:
                        if param.isalnum() and param not in metas and param != '':
                            error_dict = {'severity': 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                          'description': "FUNCTION_PARAMETER_NOT_PRESENT: Function parameter '" + param + "' used in function " +
                                                         fun_dict[
                                                             'function_name'] + " doesn't exist in content meta varaibles"}
                            error_list.append(error_dict)
                elif fun_dict['function_param'] not in metas and '$' not in fun_dict['function_param'] and fun_dict[
                    'function_name'] != 'HDR' and fun_dict['function_param'] != '':
                    error_dict = {'severity': 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "FUNCTION_PARAMETER_NOT_PRESENT: Function parameter '" + fun_dict[
                                      'function_param'] + "' used in function " + fun_dict[
                                                     'function_name'] + " doesn't exist in content meta varaibles"}
                    error_list.append(error_dict)
    return error_list


def check_static_text_in_function(child):
    """
    Checks any  static static text in functions other than functions.
    """
    functions = child.attrib.get("functions", None)
    error_dict = {}
    error_list = []
    pat = r'<@.*?>'
    if functions != None:
        static_text = re.sub(pat, '', functions)
    if functions != None and static_text != '':
        error_dict = {'severity': 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "STATIC_TEXT_NOT_ALLOWED_IN_FUNCTION: static text '" + static_text + "' not allowed in function"}
        error_list.append(error_dict)
    return error_list


def check_functions_present_in_contentline(child):
    """
    Checks whether functions are present in content line in cleaned parsers and gives      error if they are present
    """
    content = child.attrib.get("content", None)
    error_list = []
    error_dict = {}
    pat = r"<@.*?>"
    if content != None and re.search(pat, content):
        functions = ''.join(re.findall(pat, content))
        error_dict = {"severity": 'FATAL', 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "FUNCTIONS_NOT_ALLOWED_IN_CONTENT_LINE:functions '" + functions + "' are not allowed in content attribute.They should be written in functions attribute"}
        error_list.append(error_dict)
    return error_list


def check_envision_footprints_present_or_not(child):
    """
    Checks the envision footprints  like level,parsed,parsedefvalue,tableid in messageid'd
    """
    error_list = []
    error_dict = {}
    # print ("child attribute:",child.attrib)
    if "level" in child.attrib:
        error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "ENVISION_FOOT_PRINTS_NOT_ALLOWED:attribute 'level' not allowed in cleaned parser"}
        error_list.append(error_dict)
    if "parse" in child.attrib:
        error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "ENVISION_FOOT_PRINTS_NOT_ALLOWED:attribute 'parse' not allowed in cleaned parser"}
        error_list.append(error_dict)
    if "parsedefvalue" in child.attrib:
        error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "ENVISION_FOOT_PRINTS_NOT_ALLOWED:attribute 'parsedefvalue' not allowed in cleaned parser"}
        error_list.append(error_dict)
    if "tableid" in child.attrib:
        error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "ENVISION_FOOT_PRINTS_NOT_ALLOWED:attribute 'tableid' not allowed in cleaned parser"}
        error_list.append(error_dict)
    return error_list


def check_for_empty_variavles(child):
    """
    Checks for empty variables of type <> in content lines
    """
    error_list = []
    error_dict = {}
    pat = r'<>'
    content = child.attrib.get("content", None)
    if content != None and re.search(pat, content):
        error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                      'description': "EMPTY_VARIABLE_NOT_ALLOWED: Empty variables of type <> are not allowed in the content line"}
        error_list.append(error_dict)
    return error_list


def check_for_duplicate_functions(child):
    """
    Function checks for duplicate functions
    """
    error_list = []
    error_dict = {}
    functions_seen = []
    if "functions" in child.attrib:
        functions = child.attrib["functions"]
        pat = r'<@.*?>'
        functions = re.findall(pat, functions)
        for function in functions:
            if function in functions_seen:
                error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                              'description': "DUPLICATE_FUNCTIONS_FOUND:duplicate function '" + function + "'found"}
                error_list.append(error_dict)
            functions_seen.append(function)
    return error_list


def check_for_duplicate_metas(child):
    """
     Function checks for duplicate metas used in content line
    """
    error_list = []
    error_dict = {}
    metas_seen = []
    OR_block_metas_seen = []
    if "content" in child.attrib and "tagval" not in child.attrib:
        content = child.attrib["content"]
        content = re.sub('<<<', '<', content)
        content = re.sub('<<', '', content)
        pat = r'<\w+>|<\w+\.\w+>|<\w+\.\w+\.\w+>'
        pat2 = r'\{.*?\}'
        OR_block = re.findall(pat2, content)
        non_OR_block = re.sub(pat2, '', content)
        metas_non_or = re.findall(pat, non_OR_block)
        OR_block = ''.join(OR_block)
        OR_block = OR_block.replace('{', '').replace('}', '')
        OR_block_groups = OR_block.split("|")
        for meta in metas_non_or:
            if meta.startswith('space'):
                continue
            if meta in metas_seen:
                error_dict = {"severity": "ERROR", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                              'description': "DUPLICATE_META_VARIABLE_FOUND:duplicate meta '" + meta.strip('<').strip(
                                  '>') + "'found"}
                error_list.append(error_dict)
            metas_seen.append(meta)
        for group in OR_block_groups:
            OR_block_metas_seen = []
            metas = re.findall(pat, group)
            for meta in metas:
                if meta.startswith('space'):
                    continue
                if meta in OR_block_metas_seen or meta in metas_non_or:
                    error_dict = {"severity": "ERROR", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "DUPLICATE_META_VARIABLE_FOUND:duplicate meta '" + meta.strip(
                                      '<').strip('>') + "'found"}
                    error_list.append(error_dict)
                OR_block_metas_seen.append(meta)
    return error_list


def check_opening_and_closing_lt_gt(child):
    """
    Function checks whether each lt is closed with gt or not
    """
    error_list = []
    error_dict = {}
    if "content" in child.attrib:
        content = child.attrib["content"]
        content = re.sub(r'<<[\w\s]+>','',content)
        content = re.sub('<</\w+>','',content)
        content = re.sub(r'<\w+-\w+>','',content)
        content = re.sub('>>\w+>>','',content)
        content = re.sub('<[;:&]+\w+>','',content)   
        content = re.sub('<<\w+>', '', content)
        content = re.sub('<<', '', content)
        content = re.sub('>>', '>', content)
        content = re.sub('<\w+>', '', content)
        content = re.sub(r'<\w+\.\w+>|<\w+\.\w+\.\w+>','',content)
        #content = re.sub('<<\w+','',content)
        # print ("Content",content)
        matches = re.findall("<\w+|\w+>", content)
        if len(matches) != 0:
            # print ("MATCHES------------>:",matches)
            for match in matches:
                if match.startswith("<"):
                    error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "VARIABLE_NOT_CLOSED_PROPERLY: Variable '" + str(
                                      match.strip("<")) + "' should close with '>'"}
                    error_list.append(error_dict)
                elif match.endswith(">"):
                    error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "VARIABLE_NOT_CLOSED_PROPERLY: Variable '" + str(
                                      match) + "' should start with '<'"}
                    error_list.append(error_dict)

    return error_list


def check_ECT_generator_values(child):
    """
    Checks the values assigned to @EC_ACTIVITY,@EC_THEME,@EC_SUBJECT,;@ec_outcome are correct or not.
    """
    Subject_list = ['Agent', 'Calendar', 'Certificate', 'Configuration', 'CryptoKey', 'Database', 'EmailAddress',
                    'File', 'Group', 'License', 'Mailbox', 'Message', 'NetworkComm', 'OS', 'Password', 'Permission',
                    'Process', 'Registry', 'Service', 'SignatureDB', 'Time', 'User', 'Virus']
    Activity_list = ['Copy', 'Create', 'Delete', 'Deny', 'Detect', 'Disable', 'Enable', 'Execute', 'Lockout', 'Logoff',
                     'Logon', 'Modify', 'Permit', 'Read', 'Receive', 'Request', 'Restore', 'Scan', 'Send', 'Start',
                     'Stop']
    Theme_list = ['ALM', 'AccessControl', 'Authentication', 'Communication', 'Configuration', 'Encryption', 'Password',
                  'Policy', 'TEV', 'UserGroup']
    Outcome_list = ['Error', 'Failure', 'Success', 'Unknown']
    error_list = []
    if "functions" in child.attrib:
        functions = child.attrib["functions"]
        functions = re.findall('<@\w+:\w+>', functions)
        functions = [function.strip("<").strip(">") for function in functions]
        for function in functions:
            if "ec_subject" in function:
                function = function.split(":")
                function_name = function[0]
                function_value = function[1]
                if function_value not in Subject_list:
                    error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "ECT_VALUE_NOT_ALLOWED:variable '" + str(
                                      function_value) + "' is not allowed since it is not listed in ec_subject values"}
                    error_list.append(error_dict)
            if "ec_activity" in function:
                function = function.split(":")
                function_name = function[0]
                function_value = function[1]
                if function_value not in Activity_list:
                    error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "ECT_VALUE_NOT_ALLOWED:variable '" + str(
                                      function_value) + "' is not allowed since it is not listed in ec_activity values"}
                    error_list.append(error_dict)
            if "ec_theme" in function:
                function = function.split(":")
                function_name = function[0]
                function_value = function[1]
                if function_value not in Theme_list:
                    error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "ECT_VALUE_NOT_ALLOWED:variable '" + str(
                                      function_value) + "' is not allowed since it is not listed in ec_theme values"}
                    error_list.append(error_dict)
            if "ec_outcome" in function:
                function = function.split(":")
                function_name = function[0]
                function_value = function[1]
                if function_value not in Outcome_list:
                    error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                                  'description': "ECT_VALUE_NOT_ALLOWED:variable '" + str(
                                      function_value) + "' is not allowed since it is not listed in ec_outcome values"}
                    error_list.append(error_dict)
    return error_list


def check_event_category_is_valid_or_not(child):
    """
    function checks whether eventcategory value is valid or not.
    """
    event_category_list = ['1000000000', '1001000000', '1001010000', '1001020000', '1001020100', '1001020200',
                           '1001020201', '1001020202', '1001020203', '1001020204', '1001020205', '1001020206',
                           '1001020300', '1001020301', '1001020302', '1001020303', '1001020304', '1001020305',
                           '1001020306', '1001020307', '1001020308', '1001020309', '1001030000', '1001030100',
                           '1001030200', '1001030201', '1001030202', '1001030203', '1001030300', '1001030301',
                           '1001030302', '1001030303', '1001030304', '1001030305', '1001030400', '1001030500',
                           '1002000000', '1002010000', '1002010100', '1002010200', '1002020000', '1002030000',
                           '1002040000', '1002050000', '1002060000', '1003000000', '1003010000', '1003010100',
                           '1003010200', '1003010300', '1003010400', '1003010500', '1003010600', '1003010700',
                           '1003010800', '1003010900', '1003011000', '1003020000', '1003030000', '1003040000',
                           '1003050000', '1100000000', '1101000000', '1101010000', '1101020000', '1102000000',
                           '1103000000', '1103010000', '1103020000', '1103030000', '1104000000', '1200000000',
                           '1201000000', '1201010000', '1202000000', '1203000000', '1204000000', '1204010000',
                           '1204010100', '1204010200', '1204010300', '1204010400', '1204020000', '1204020100',
                           '1204020200', '1204020300', '1204020400', '1205000000', '1205010000', '1205020000',
                           '1206000000', '1206010000', '1206020000', '1207000000', '1207010000', '1207010100',
                           '1207010200', '1207010201', '1207020000', '1207020100', '1207030000', '1207030100',
                           '1207040000', '1207040100', '1207040200', '1300000000', '1301000000', '1301010000',
                           '1301020000', '1302000000', '1302010000', '1302010100', '1302010200', '1302010300',
                           '1302010400', '1303000000', '1304000000', '1400000000', '1401000000', '1401010000',
                           '1401020000', '1401030000', '1401040000', '1401050100', '1401050200', '1401060000',
                           '1401060100', '1401070000', '1401070100', '1401080000', '1401090000', '1402000000',
                           '1402010100', '1402010200', '1402010300', '1402010301', '1402010302', '1402020100',
                           '1402020200', '1402020300', '1402020400', '1402030000', '1402040100', '1402040101',
                           '1402040200', '1500000000', '1501000000', '1501010000', '1501020000', '1501030000',
                           '1501040000', '1501040100', '1501050000', '1501050100', '1502000000', '1502010000',
                           '1502020000', '1502030000', '1502040000', '1502050000', '1503000000', '1503010100',
                           '1503020200', '1600000000', '1601000000', '1601010000', '1601020000', '1602000000',
                           '1602010000', '1602020000', '1602020100', '1603000000', '1603010000', '1603010100',
                           '1603020000', '1603030000', '1603040000', '1603050000', '1603060000', '1603070000',
                           '1603080000', '1603090000', '1603100000', '1603110000', '1604000000', '1604010000',
                           '1605000000', '1605010000', '1605020000', '1605030000', '1606000000', '1607000000',
                           '1608000000', '1608010000', '1609000000', '1610000000', '1611000000', '1612000000',
                           '1612010000', '1613010000', '1613020000', '1613030000', '1613030100', '1613040100',
                           '1613040200', '1613050100', '1613050200', '1613050201', '1613060100', '1613060200',
                           '1614000000', '1614010000', '1614020000', '1614030000', '1700000000', '1701000000',
                           '1701010000', '1701020000', '1701030000', '1701040000', '1701050000', '1701060000',
                           '1701070000', '1701080000', '1702000000', '1702010000', '1702020000', '1702030000',
                           '1703000000', '1703010000', '1703020000', '1704000000', '1704010000', '1704020000',
                           '1704030000', '1705010000', '1705010100', '1705010200', '1800000000', '1801000000',
                           '1801010000', '1801010100', '1801020000', '1801020100', '1801030000', '1801030100',
                           '1802000000', '1803000000', '1803010000', '1803020000', '1803030000', '1804000000',
                           '1804010000', '1804020000', '1805000000', '1805010000', '1805010100', '1805020000',
                           '1900000000', '1901000000']
    error_list = []
    deprecated_list = ['1614010000','1614020000','1701080000','1702020000','1703010000','1900000000','1804020000','1800000000','1705010200','1700000000','1605030000','1603060000','1503020200','1503010100','1503000000','1502020000','1502010000','1501040000','1501010000','1500000000','1401090000','401080000','1401020000','1400000000','1302010000','1301020000','1300000000','1207030100','1207030000','1207020100','1203000000','1202000000','1200000000','1100000000','1003011000','1003010900','1003010800','1003010700','1003010600','1003010500','1003010400','1003010300','1000000000','1001010000','1001030100','1001030201','1001030400','1003010100','1003010200','1003010300','1003010400','1003010500','1003010600','1003010700','1003010800','1003010900','1003011000']
    if "eventcategory" in child.attrib:
        eventcategory = child.attrib["eventcategory"]
        if eventcategory not in event_category_list:
            error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                          'description': "INVALID_EVENT_CATEGORY_VALUE:value '" + str(
                              eventcategory) + "' is not allowed since it is not listed in eventcategory variables list"}
            error_list.append(error_dict)
    if "eventcategory" in child.attrib:
        eventcategory = child.attrib["eventcategory"]
        if eventcategory in deprecated_list:
            error_dict = {"severity": "FATAL", 'id1': "Messageid: " + child.attrib.get('id1', 'None'),
                          'description': "DEPRECARED_EVENT_CATEGORY_VALUE:value '" + str(
                              eventcategory) + "' is not allowed since it is deprecated."}
            error_list.append(error_dict)        
    return error_list


def check_ini_tags_are_present_or_not(root):
    """
    checks ini file contents name,displayname,type and groups are present or not
    """
    error_list = []
    ini_tags = ["name", "displayname", "group"]
    for tag in ini_tags:
        if tag not in root.attrib:
            error_dict = {"severity": "FATAL", 'id1': 'DEVICEMESSAGE',
                          'description': "INI_FILE_CONTENT_NOT_FOUND  ini content tag '" + str(
                              tag) + "'not found in parser"}
            error_list.append(error_dict)
    return error_list


def validate_schema(source_file, schema_file):
    """
    Checks whether the xml is valid against the schema or not
    """
    with open(schema_file, encoding="utf8") as f_schema:
        try:
            schema_doc = ET.parse(f_schema)
            schema = ET.XMLSchema(schema_doc)
            parser = ET.XMLParser(schema=schema)
        except Exception as e:
            return e

        with open(source_file, encoding="utf8") as f_source:
            try:
                doc = ET.parse(f_source, parser)
                return True
            except ET.XMLSyntaxError as e:
                # this exception is thrown on schema validation error
                return e
            except Exception as e:
                return e

def check_duplicate_tags_for_cef(child):
    """
        checks for duplicate tags in cef
        """
    tag = child.attrib['cefName']
    error_dict = {}
    error_list = []
    if tag in tag_seen:
        error_dict = {'severity': 'FATAL', 'cef tag': "cefName =" + tag,'id1': 'ExtensionKey',
                      'description': 'DUPLICATE_CEF_TAG_FOUND:cefName="'+tag+'"'}
        error_list.append(error_dict)
    tag_seen.append(tag)

    return error_list
def display_errors(list_of_error_nodes, Fatals, Errors, Warnings, output_file, parser_dir, schema_validation):
    """
    This function displays the output in the html format
    """
    errors_found = []
    error_seen = []
    for node in list_of_error_nodes:
        errors_found += node.errors_found
    # print ("Errors found:",errors_found)
    Fatals_found = [error for error in errors_found if error != {} and error['severity'] == 'FATAL']
    Fatals = len(Fatals_found)
    errors_found = [error for error in errors_found if error != {} and error['severity'] == 'ERROR']
    # print ("errors_found",errors_found)
    Errors = len(errors_found)
    #print ("Errors:", Errors, "\n", "Fatals:", Fatals)
    device = output_file.replace("_output.html", '')
    #print ("device",device)
   #print ("error",errors_found)
    output_file = os.path.join(parser_dir, output_file)
    htmlstr = "<html><center><font color='red'><h1>RSA Syntax Checker</h1></font></br><font color='green'><h2>Device name:" + device + "</h2><h2><font color='green'>Checked:" + str(
        len(header_id_seen)) + " headers and " + str(len(
        message_id_seen)) + " messageids</font></h2></font></br></br><table border='solid'><tr><th>severirity</th><th>Total</th></tr><tr><td>Fatals</td><td><font color='red'>" + str(
        Fatals) + "</td></font></tr><tr><td>Errors</td><td><font color='red'>" + str(
        Errors) + "</font></td></tr><tr><td>Warnings</td><td><font color='red'>" + str(
        Warnings) + "</font></td></tr></table></br><table border='1'><tr><th>Schema validation status</th><th>Failure Reason</th></tr><tr><td>" + \
              schema_validation['status'] + "</td><td>" + schema_validation[
                  'FAILURE_REASON'] + "</td></tr></table></center></br>"
    f = open(output_file, "w+")
    if len(Fatals_found) != 0:
        htmlstr += "<center><h2><font color='red'>FATAL DETAILS:</font></h2><table border='solid' style='border: 2px solid black'><tr><th>Sr.No</th><th>severity</th><th>Headerid/Messageid</th><th>Description</th><tr>"
        for i, error in enumerate(Fatals_found):
            error_seen.append(error)
            if "Header" in error['id1']:
                attribute = 'Header'
            elif "Messageid" in error['id1']:
                attribute = "Messageid"
            else:
                attribute = ''
            id=error['id1'].replace('Messageid','').replace("Headerid",'')
            #id=error['id1'].replace('Messageid').replace("Headerid")
            id = attribute + ":<font color='blue'>"+id+"</font>"
            id=id.replace('::',':')
            htmlstr += "<tr><td>" + str(i + 1) + "</td><td>" + error[
                'severity'] + "</td><td>" + id + "</td><td width='7000'><font color='red'>" + error[
                           'description'] + "</font></td><tr>"
        htmlstr += "</table></center></html>"
    if len(errors_found) != 0:
        htmlstr += "<center><h2><font color='red'>ERROR DETAILS:</font></h2><table border='solid' style='border: 2px solid black'><tr><th>Sr.No</th><th>severity</th><th>Headerid/Messageid</th><th>Description</th><tr>"
        for i, error in enumerate(errors_found):
            error_seen.append(error)
            if "Header" in error['id1']:
                attribute = 'Header'
            elif "Messageid" in error['id1']:
                attribute = "Messageid"
            else:
                attribute = ''
            id=error['id1'].replace('Messageid','').replace("Headerid",'')
            #id=error['id1'].replace('Messageid').replace("Headerid")
            id = attribute + ":<font color='blue'>"+id+"</font>"
            id=id.replace('::',':')
            htmlstr += "<tr><td>" + str(i + 1) + "</td><td>" + error[
                'severity'] + "</td><td>" + id + "</td><td width='7000'><font color='red'>" + error[
                           'description'] + "</font></td><tr>"
        htmlstr += "</table></center></html>"
    #print ("Writing data to the file")    
    f.write(htmlstr)
    #print("written")
    f.flush()
    f.close()
    wb.open(output_file)

def main():
    if len(sys.argv) < 2:
        print ("Usage:\n\tpython syntax_checker.py <Parser_name> [<output_directory>]")
        sys.exit(0)

    parser_file_name = sys.argv[1]
    parser_dir, parser_name = os.path.split(parser_file_name)
    output_file = os.path.splitext(parser_name)[0].replace("msg", '').replace("v20_", "") + "_output.html"
    # errors_found = []
    if len(sys.argv) == 3:
        output_dir = sys.argv[2]
    else:
        output_dir = parser_dir
    list_of_error_nodes = []  # This will have a list of all the error nodes
    Fatals = 0
    Errors = 0
    Warnings = 0
    source_file = parser_file_name
    schema_file = 'eventsourcemsg.xsd'
    status = validate_schema(source_file, schema_file)
    schema_validation = {}
    if status != True:
        print ("Schema is not valid:", status)
        # f= open(output_file,"w")
        # f.write("<html><center><h3><font color='red'>Schema validation failed:"+str(status)+"</font></h3></center></html>")
        # wb.open(output_file)
        # sys.exit(0)
        schema_validation["status"] = "<font color='red'>FAILED</font>"
        schema_validation["FAILURE_REASON"] = "<font color='red'>" + str(status) + "</font>"
    else:
        schema_validation["status"] = "<font color='green'>SUCCEEDED</font>"
        schema_validation["FAILURE_REASON"] = "<font color='green'>N/A</font>"

    tree = ET.parse(parser_file_name)
    root = tree.getroot()
    if not parser_file_name.endswith('cef.xml'):
        error_list = check_ini_tags_are_present_or_not(root)
        if len(error_list) != 0:
            node = Error_Node(root)
            node.errors_found += error_list
            list_of_error_nodes.append(node)
            Fatals += len(error_list)
    for child in root:
        node = Error_Node(child)  # This will get instantiated at the beginning of each loop
        # check for headers
        if child.tag == 'HEADER':
            # check all header attributes are present or not
            error_list = check_all_header_attributes_present(child)
            node.errors_found += error_list
            Fatals += len(error_list)
            if "id1" in child.attrib and "id2" in child.attrib:
                # check whether header id1 and id2 are equal or not
                error_list = check_header_id_equality(child)
                node.errors_found += error_list
                Fatals = Fatals + len(error_list)

                # check whether header  id1 and id2 are integers or not
                error_list = check_header_ids_integers_or_not(child)
                node.errors_found += error_list
                Fatals += len(error_list)

                # check duplicate_header_ids
                error_list = check_duplicate_header_id(child)
                node.errors_found += error_list
                Fatals = Fatals + len(error_list)

                # check for messageid meta if messageid tag exists for a header
                error_list = check_messageid_tag_and_content_line_meta(child)
                node.errors_found += error_list
                Fatals = Fatals + len(error_list)
                # checks for messageid's
        if child.tag == 'MESSAGE':
            # check all messageid attributes are present or not
            error_list = check_all_messageid_attributes_present(child)
            node.errors_found += error_list
            Fatals += len(error_list)
            # Check for duplicate messageid
            if "id1" in child.attrib and "id2" in child.attrib:
                error_list = check_duplicate_message_id(child)
                node.errors_found += error_list
                Fatals = Fatals + len(error_list)

                # check whether meta present in table-map.xml
                error_list = check_meta_present_in_MVG(child)
                node.errors_found += error_list
                Errors += len(error_list)

                # Special characters in messageid id1 and id2 attribute
                error_list = check_special_characters_in_messageid(child)
                node.errors_found += error_list
                Errors += len(error_list)

                # Check all function parameters present in metas
                error_list = check_function_parameter_name_exists_in_metas(child)
                node.errors_found += error_list
                Fatals += len(error_list)

                # Check any static text in function attribute
                error_list = check_static_text_in_function(child)
                node.errors_found += error_list
                Fatals += len(error_list)

                # Check any functions present in content line attribute
                error_list = check_functions_present_in_contentline(child)
                node.errors_found += error_list
                Fatals += len(error_list)

                # Check envision footprints are present or not in the parser
                error_list = check_envision_footprints_present_or_not(child)
                node.errors_found += error_list
                Fatals += len(error_list)

                # Check for empty variables in content line
                error_list = check_for_empty_variavles(child)
                node.errors_found += error_list
                Fatals += len(error_list)

                # Check for duplicate functions
                error_list = check_for_duplicate_functions(child)
                node.errors_found += error_list
                Fatals += len(error_list)

                # Check for duplicate meta variables
                error_list = check_for_duplicate_metas(child)
                node.errors_found += error_list
                Errors += len(error_list)


                # check for correct opening and closing < and > tags
                error_list = check_opening_and_closing_lt_gt(child)
                node.errors_found += error_list
                Errors += len(error_list)

                # ECT values check
                error_list = check_ECT_generator_values(child)
                node.errors_found += error_list
                Errors += len(error_list)

                # eventcategory validation
                error_list = check_event_category_is_valid_or_not(child)
                node.errors_found += error_list
                Errors += len(error_list)

        #Check if there are any duplicate tags present in cef.xml
        if child.tag == 'ExtensionKeys':
            for subElement in child:
                if subElement.tag == 'ExtensionKey':
                    error_list = check_duplicate_tags_for_cef(subElement)
                    node.errors_found += error_list
                    Fatals += len(error_list)

        if node.errors_found != []:
            # print ("Node--------->",node)
            list_of_error_nodes.append(node)
            #list_of_error_nodes.extend(ce)
    # print ("Fatals:",Fatals,"errors:",Errors)
    display_errors(list_of_error_nodes, Fatals, Errors, Warnings, output_file, output_dir, schema_validation)

if __name__ == "__main__":
    main()