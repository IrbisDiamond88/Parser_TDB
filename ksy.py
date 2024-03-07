# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Tinydb(KaitaiStruct):

    class Tcompresslevel(Enum):
        clmaximum = 0
        clnormal = 1
        clfast = 2
        clsuperfast = 3

    class Tencryptmode(Enum):
        emcts = 0
        emcbc = 1
        emcfb = 2
        emofb = 3
        emecb = 4

    class Bool(Enum):
        false = 0
        true = 1

    class Tfielddataprocessmode(Enum):
        fddefault = 0
        fdoriginal = 1

    class Tfieldtype(Enum):
        ftunknown = 0
        ftstring = 1
        ftsmallint = 2
        ftinteger = 3
        ftword = 4
        ftboolean = 5
        ftfloat = 6
        ftcurrency = 7
        ftbcd = 8
        ftdate = 9
        fttime = 10
        ftdatetime = 11
        ftbytes = 12
        ftvarbytes = 13
        ftautoinc = 14
        ftblob = 15
        ftmemo = 16
        ftgraphic = 17
        ftfmtmemo = 18
        ftparadoxole = 19
        ftdbaseole = 20
        fttypedbinary = 21
        ftcursor = 22
        ftfixedchar = 23
        ftwidestring = 24
        ftlargeint = 25
        ftadt = 26
        ftarray = 27
        ftreference = 28
        ftdataset = 29
        ftorablob = 30
        ftoraclob = 31
        ftvariant = 32
        ftinterface = 33
        ftidispatch = 34
        ftguid = 35
        fttimestamp = 36
        ftfmtbcd = 37
        ftfixedwidechar = 38
        ftwidememo = 39
        ftoratimestamp = 40
        ftorainterval = 41
        ftlongword = 42
        ftshortint = 43
        ftbyte = 44
        ftextended = 45
        ftconnection = 46
        ftparams = 47
        ftstream = 48
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.fileheader = Tinydb.Tfileheader(self._io, self, self._root)
        self.textdatablock = Tinydb.Ttextdatablock(self._io, self, self._root)
        self.dboptions = Tinydb.Tdboptions(self._io, self, self._root)
        self.tabletab = Tinydb.Ttabletab(self._io, self, self._root)
        self.tables = []
        for i in range(self.tabletab.tablecount):
            self.tables.append(Tinydb.Ttableheader(self.tabletab.tableheaderoffset[i], self._io, self, self._root))


    class Ftdate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.datebin = self._io.read_s4le()


    class Ttextdatablock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.comments = (self._io.read_bytes(257)).decode(u"windows-1251")
            self.data = (self._io.read_bytes(2048)).decode(u"windows-1251")


    class Tfileheader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.softname = (self._io.read_bytes(7)).decode(u"windows-1251")
            self.filefmtver = (self._io.read_bytes(5)).decode(u"windows-1251")


    class Tfieldtabitem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.fieldname = (self._io.read_bytes(33)).decode(u"windows-1251")
            self.fieldtype = KaitaiStream.resolve_enum(Tinydb.Tfieldtype, self._io.read_u1())
            self.fieldsize = self._io.read_s4le()
            self.dpmode = KaitaiStream.resolve_enum(Tinydb.Tfielddataprocessmode, self._io.read_u1())
            self.reserved = self._io.read_s4le()


    class Ttabletab(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tablecount = self._io.read_s4le()
            self.reserved = self._io.read_s4le()
            self.tableheaderoffset = []
            for i in range(256):
                self.tableheaderoffset.append(self._io.read_s4le())



    class Tdboptions(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.compressblob = KaitaiStream.resolve_enum(Tinydb.Bool, self._io.read_u1())
            self.compresslevel = KaitaiStream.resolve_enum(Tinydb.Tcompresslevel, self._io.read_u1())
            self.compressalgoname = (self._io.read_bytes(33)).decode(u"windows-1251")
            self.encrypt = KaitaiStream.resolve_enum(Tinydb.Bool, self._io.read_u1())
            self.encryptmode = KaitaiStream.resolve_enum(Tinydb.Tencryptmode, self._io.read_u1())
            self.encryptalgoname = (self._io.read_bytes(33)).decode(u"windows-1251")
            self.crc32 = KaitaiStream.resolve_enum(Tinydb.Bool, self._io.read_u1())
            self.randombuffer = self._io.read_bytes(256)
            self.hashpassword = self._io.read_bytes(129)
            self.reserved = self._io.read_bytes(16)


    class Ttableheader(KaitaiStruct):
        def __init__(self, offset, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.offset = offset
            self._read()

        def _read(self):
            pass

        @property
        def tableheader(self):
            if hasattr(self, '_m_tableheader'):
                return self._m_tableheader

            _pos = self._io.pos()
            self._io.seek(self.offset)
            self._m_tableheader = Tinydb.Ttableheader2(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_tableheader', None)


    class Fttime(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timebin = self._io.read_s4le()

        @property
        def hours(self):
            if hasattr(self, '_m_hours'):
                return self._m_hours

            self._m_hours = self.timebin // 3600000
            return getattr(self, '_m_hours', None)

        @property
        def mins(self):
            if hasattr(self, '_m_mins'):
                return self._m_mins

            self._m_mins = (self.timebin - (self.hours * 3600000)) // 60000
            return getattr(self, '_m_mins', None)

        @property
        def secs(self):
            if hasattr(self, '_m_secs'):
                return self._m_secs

            self._m_secs = ((self.timebin - (self.hours * 3600000)) - (self.mins * 60000)) // 1000
            return getattr(self, '_m_secs', None)


    class Ttableheader2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tablename = (self._io.read_bytes(33)).decode(u"windows-1251")
            self.rectaboffset = self._io.read_s4le()
            self.recordtotal = self._io.read_s4le()
            self.autoinccounter = self._io.read_s4le()
            self.fieldcount = self._io.read_s4le()
            self.fieldtab = []
            for i in range(96):
                self.fieldtab.append(Tinydb.Tfieldtabitem(self._io, self, self._root))

            self.indexcount = self._io.read_s4le()
            self.indexheader = []
            for i in range(8):
                self.indexheader.append(Tinydb.Tindexheader(self._io, self, self._root))

            self.reserved = self._io.read_bytes(16)

        @property
        def rectable(self):
            if hasattr(self, '_m_rectable'):
                return self._m_rectable

            _pos = self._io.pos()
            self._io.seek(self.rectaboffset)
            self._m_rectable = Tinydb.Trecordblock(self.recordtotal, self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_rectable', None)


    class Trecordblock(KaitaiStruct):
        def __init__(self, n, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.n = n
            self._read()

        def _read(self):
            self.nextblock = self._io.read_s4le()
            self.table = []
            for i in range(self.n):
                self.table.append(Tinydb.Trecordtabitem(self._io, self, self._root))



    class Tindexheader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.indexname = (self._io.read_bytes(33)).decode(u"windows-1251")
            self.indexoptions = self._io.read_bytes(32)
            self.fieldidx = []
            for i in range(8):
                self.fieldidx.append(self._io.read_s4le())

            self.indexoffset = self._io.read_s4le()
            self.startindex = self._io.read_s4le()
            self.reserved = self._io.read_s4le()


    class Trecordtabitem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dataoffset = self._io.read_s4le()
            self.deleteflag = KaitaiStream.resolve_enum(Tinydb.Bool, self._io.read_u1())

        @property
        def fileds(self):
            if hasattr(self, '_m_fileds'):
                return self._m_fileds

            _pos = self._io.pos()
            self._io.seek(self.dataoffset)
            self._m_fileds = []
            for i in range(self._parent._parent.fieldcount):
                _on = self._parent._parent.fieldtab[i].fieldtype
                if _on == Tinydb.Tfieldtype.ftsmallint:
                    self._m_fileds.append(self._io.read_u2le())
                elif _on == Tinydb.Tfieldtype.ftinteger:
                    self._m_fileds.append(self._io.read_s4le())
                elif _on == Tinydb.Tfieldtype.ftdate:
                    self._m_fileds.append(Tinydb.Ftdate(self._io, self, self._root))
                elif _on == Tinydb.Tfieldtype.ftfloat:
                    self._m_fileds.append(self._io.read_f8le())
                elif _on == Tinydb.Tfieldtype.ftstring:
                    self._m_fileds.append(Tinydb.Tstring((self._parent._parent.fieldtab[i].fieldsize + 1), self._io, self, self._root))
                elif _on == Tinydb.Tfieldtype.fttime:
                    self._m_fileds.append(Tinydb.Fttime(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_fileds', None)


    class Tstring(KaitaiStruct):
        def __init__(self, length, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.length = length
            self._read()

        def _read(self):
            self.text = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.length), 0, False)).decode(u"windows-1251")



