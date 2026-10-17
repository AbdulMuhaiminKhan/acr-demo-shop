import os

INVOICE_DIR = "/srv/shop/invoices"


def invoice_path(filename: str) -> str:
    return os.path.join(INVOICE_DIR, filename)


def read_invoice(filename: str) -> bytes:
    try:
        with open(invoice_path(filename), "rb") as fh:
            return fh.read()
    except Exception:
        pass
    return b""
