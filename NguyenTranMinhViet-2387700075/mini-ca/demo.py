import os
from cryptography import x509
from ca_utils import create_root_ca, create_intermediate_ca, issue_certificate, verify_certificate_chain, load_cert
from revoke_utils import revoke_certificate, check_revocation_status, create_empty_crl

def setup_ca():
    print("Tạo Root CA...")
    root_key, root_cert = create_root_ca()
    print("Tạo Intermediate CA...")
    inter_key, inter_cert = create_intermediate_ca(root_key, root_cert)
    create_empty_crl(inter_cert, inter_key)

def issue_cert_demo():
    print("Phát hành chứng chỉ người dùng cuối...")
    inter_key = load_key_safe(os.path.join("certs", "intermediate_key.pem"))
    inter_cert = load_cert(os.path.join("certs", "intermediate_cert.pem"))
    subject_info = {
        "common_name": "Phuoc_Nguyen",
        "org": "PHUOCNTMH Company",
        "country": "VN"
    }
    cert_key, cert = issue_certificate(inter_key, inter_cert, subject_info)
    print(f"Đã phát hành: certs\\Phuoc_Nguyen_cert.pem, certs\\Phuoc_Nguyen_key.pem")
    return os.path.join("certs", "Phuoc_Nguyen_cert.pem")

def load_key_safe(path):
    from ca_utils import load_key
    return load_key(path)

def verify_chain_demo(user_cert_path):
    print("Kiểm tra chuỗi chứng chỉ...")
    chain_paths = [
        os.path.join("certs", "intermediate_cert.pem"),
        os.path.join("certs", "root_ca_cert.pem")
    ]
    chain_certs = [load_cert(p) for p in chain_paths]
    user_cert = load_cert(user_cert_path)
    valid = verify_certificate_chain(user_cert, chain_certs)
    print(f"Chuỗi hợp lệ: {valid}")
    return valid

def revoke_demo():
    print("Thu hồi chứng chỉ user1...")
    revoke_certificate(
        os.path.join("certs", "Phuoc_Nguyen_cert.pem"),
        os.path.join("certs", "intermediate_cert.pem"),
        os.path.join("certs", "intermediate_key.pem"),
        reason=x509.ReasonFlags.key_compromise
    )
    print("Đã thu hồi")

def ocsp_check_demo():
    print("Kiểm tra trạng thái OCSP của Phuoc_Nguyen_cert.pem...")
    status = check_revocation_status(os.path.join("certs", "Phuoc_Nguyen_cert.pem"))
    print(f"Trạng thái: {'Revoked' if status else 'Valid'}")

def run_all():
    setup_ca()
    user_cert = issue_cert_demo()
    verify_chain_demo(user_cert)
    revoke_demo()
    ocsp_check_demo()

if __name__ == "__main__":
    run_all()