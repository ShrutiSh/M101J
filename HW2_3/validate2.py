import base64
code="CmltcG9ydCBweW1vbmdvCmltcG9ydCB1cmxsaWIyCmltcG9ydCB1cmxsaWIKaW1wb3J0IGNvb2tpZWxpYgppbXBvcnQgcmFuZG9tCmltcG9ydCByZQppbXBvcnQgc3RyaW5nCgojIG1ha2VzIGEgbGl0dGxlIHNhbHQKZGVmIG1ha2Vfc2FsdChuKToKICAgIHNhbHQgPSAiIgogICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgICAgc2FsdCA9IHNhbHQgKyByYW5kb20uY2hvaWNlKHN0cmluZy5hc2NpaV9sZXR0ZXJzKQogICAgcmV0dXJuIHNhbHQKCgojIHRoaXMgaXMgYSB2YWxpZGF0aW9uIHByb2dyYW0gdG8gbWFrZSBzdXJlIHRoYXQgdGhlIGJsb2cgd29ya3MgY29ycmVjdGx5LgoKZGVmIGNyZWF0ZV91c2VyKHVzZXJuYW1lLCBwYXNzd29yZCk6CiAgICB0cnk6CiAgICAgICAgcHJpbnQgIlRyeWluZyB0byBjcmVhdGUgYSB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUKICAgICAgICBjaiA9IGNvb2tpZWxpYi5Db29raWVKYXIoKQogICAgICAgIHVybCA9ICJodHRwOi8vbG9jYWxob3N0OjgwODIvc2lnbnVwIgoKICAgICAgICBkYXRhID0gdXJsbGliLnVybGVuY29kZShbKCJlbWFpbCIsIiIpLCgidXNlcm5hbWUiLHVzZXJuYW1lKSwgKCJwYXNzd29yZCIscGFzc3dvcmQpLCAoInZlcmlmeSIscGFzc3dvcmQpXSkKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwsIGRhdGE9ZGF0YSkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcih1cmxsaWIyLkhUVFBDb29raWVQcm9jZXNzb3IoY2opKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKICAgICAgICAjIGNoZWNrIHRoYXQgdGhlIHVzZXIgaXMgaW4gdGhlIHVzZXIgdGFibGUKICAgICAgICBjb25uZWN0aW9uID0gcHltb25nby5Db25uZWN0aW9uKCJtb25nb2RiOi8vbG9jYWxob3N0Iiwgc2FmZT1UcnVlKQogICAgICAgIGRiID0gY29ubmVjdGlvbi5ibG9nCiAgICAgICAgdXNlcnMgPSBkYi51c2VycwogICAgICAgIHVzZXIgPSB1c2Vycy5maW5kX29uZSh7J19pZCc6dXNlcm5hbWV9KQogICAgICAgIGlmICh1c2VyID09IE5vbmUpOgogICAgICAgICAgICBwcmludCAiQ291bGQgbm90IGZpbmQgdGhlIHRlc3QgdXNlciAiLCB1c2VybmFtZSwgImluIHRoZSB1c2VycyBjb2xsZWN0aW9uLiIKICAgICAgICAgICAgcmV0dXJuIEZhbHNlCiAgICAgICAgcHJpbnQgIkZvdW5kIHRoZSB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUsICIgaW4gdGhlIHVzZXJzIGNvbGxlY3Rpb24iCgogICAgICAgICMgY2hlY2sgdGhhdCB0aGUgdXNlciBoYXMgYmVlbiBidWlsdAogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUoIldlbGNvbWVccysiKyB1c2VybmFtZSkKICAgICAgICBpZiBleHByLnNlYXJjaChyZXN1bHQpOgogICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgIAogICAgICAgIHByaW50ICJXaGVuIHdlIHRyaWVkIHRvIGNyZWF0ZSBhIHVzZXIsIGhlcmUgaXMgdGhlIG91dHB1dCB3ZSBnb3RcbiIKICAgICAgICBwcmludCByZXN1bHQKICAgICAgICAKICAgICAgICByZXR1cm4gRmFsc2UKICAgIGV4Y2VwdDoKICAgICAgICBwcmludCAidGhlIHJlcXVlc3QgdG8gIiwgdXJsLCAiIGZhaWxlZCwgc28geW91ciBibG9nIG1heSBub3QgYmUgcnVubmluZy4iCiAgICAgICAgcmV0dXJuIEZhbHNlCgoKZGVmIHRyeV90b19sb2dpbih1c2VybmFtZSwgcGFzc3dvcmQpOgoKICAgIHRyeToKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIGxvZ2luIGZvciB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUKICAgICAgICBjaiA9IGNvb2tpZWxpYi5Db29raWVKYXIoKQogICAgICAgIHVybCA9ICJodHRwOi8vbG9jYWxob3N0OjgwODIvbG9naW4iCgogICAgICAgIGRhdGEgPSB1cmxsaWIudXJsZW5jb2RlKFsoInVzZXJuYW1lIix1c2VybmFtZSksICgicGFzc3dvcmQiLHBhc3N3b3JkKV0pCiAgICAgICAgcmVxdWVzdCA9IHVybGxpYjIuUmVxdWVzdCh1cmw9dXJsLCBkYXRhPWRhdGEpCiAgICAgICAgb3BlbmVyID0gdXJsbGliMi5idWlsZF9vcGVuZXIodXJsbGliMi5IVFRQQ29va2llUHJvY2Vzc29yKGNqKSkKICAgICAgICBmID0gb3BlbmVyLm9wZW4ocmVxdWVzdCkKCiAgICAgICAgIyBjaGVjayBmb3Igc3VjY2Vzc2Z1bCBsb2dpbgogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUoIldlbGNvbWVccysiKyB1c2VybmFtZSkKICAgICAgICBpZiBleHByLnNlYXJjaChyZXN1bHQpOgogICAgICAgICAgICByZXR1cm4gVHJ1ZQoKICAgICAgICBwcmludCAiV2hlbiB3ZSB0cmllZCB0byBsb2dpbiwgaGVyZSBpcyB0aGUgb3V0cHV0IHdlIGdvdFxuIgogICAgICAgIHByaW50IHJlc3VsdAogICAgICAgIHJldHVybiBGYWxzZQogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJ0aGUgcmVxdWVzdCB0byAiLCB1cmwsICIgZmFpbGVkLCBzbyB5b3VyIGJsb2cgbWF5IG5vdCBiZSBydW5uaW5nLiIKICAgICAgICByYWlzZQogICAgICAgIHJldHVybiBGYWxzZQoKCnVzZXJuYW1lID0gbWFrZV9zYWx0KDcpCnBhc3N3b3JkID0gbWFrZV9zYWx0KDgpCgojIHRyeSB0byBjcmVhdGUgdXNlcgoKaWYgKGNyZWF0ZV91c2VyKHVzZXJuYW1lLCBwYXNzd29yZCkpOgogICAgcHJpbnQgIlVzZXIgY3JlYXRpb24gc3VjY2Vzc2Z1bC4gIgogICAgIyB0cnkgdG8gbG9naW4KICAgIGlmICh0cnlfdG9fbG9naW4odXNlcm5hbWUsIHBhc3N3b3JkKSk6CiAgICAgICAgcHJpbnQgIlVzZXIgbG9naW4gc3VjY2Vzc2Z1bC4iCiAgICAgICAgcHJpbnQgIlZhbGlkYXRpb24gQ29kZSBpcyAiLCAiZmhqODM3aGY5Mzc2aGdmOTNoZjgzMmpmOSIKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIlVzZXIgbG9naW4gZmFpbGVkIgogICAgICAgIHByaW50ICJTb3JyeSwgeW91IGhhdmUgbm90IHNvbHZlZCBpdCB5ZXQuIgoKZWxzZToKICAgIHByaW50ICJTb3JyeSwgeW91IGhhdmUgbm90IHNvbHZlZCBpdCB5ZXQuIgoKCgoKCgoKCg=="
print(base64.b64decode(code))
