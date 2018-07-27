#!/usr/bin/env python3
__Author__ = "limugen"


def send_text_to_chat(access_token, chat_id, text):
    msg_type, msg = _gen_text_msg(text)
    return _send_msg_to_chat(access_token, chat_id, msg_type, msg)

def _send_msg_to_chat(access_token, chat_id, msg_type, msg):
    body_dict = {
        "chatid": chat_id,
        "msgtype": msg_type
    }
    body_dict[msg_type] = msg
    body = json.dumps(body_dict)
    return _send_msg("https://oapi.dingtalk.com/chat/send?access_token=", access_token, body)

