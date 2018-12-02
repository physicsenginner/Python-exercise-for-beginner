def sistem_bilgisi_goster():
    import sys
    print("""Sistemde Kurulu Python'ın
          \nAna sürüm numarası:{}
          \nAlt sürüm numarası:{}
          \nMinik sürüm numarası:{}
          \nKullanılan İşletim Sistemi :{}""".format(
                sys.version_info.major,
                sys.version_info.minor,
                sys.version_info.micro,
                sys.platform
              ))

sistem_bilgisi_goster()
