"""Binary classes"""
from __future__ import print_function

import binascii
import gzip
import logging
import os
import shutil
import struct
import subprocess
import tempfile
import zipfile
from json import dumps

import pysam
from bx.seq.twobit import TWOBIT_MAGIC_NUMBER, TWOBIT_MAGIC_NUMBER_SWAP, TWOBIT_MAGIC_SIZE

from galaxy import util
from galaxy.datatypes import metadata
from galaxy.datatypes.metadata import DictParameter, ListParameter, MetadataElement, MetadataParameter
from galaxy.util import FILENAME_VALID_CHARS, nice_size, sqlite, which
from . import data, dataproviders


log = logging.getLogger(__name__)

# Currently these supported binary data types must be manually set on upload


class Binary( data.Data ):
    """Binary data"""
    edam_format = "format_2333"
    sniffable_binary_formats = []
    unsniffable_binary_formats = []

    @staticmethod
    def register_sniffable_binary_format(data_type, ext, type_class):
        Binary.sniffable_binary_formats.append({"type": data_type, "ext": ext.lower(), "class": type_class})

    @staticmethod
    def register_unsniffable_binary_ext(ext):
        Binary.unsniffable_binary_formats.append(ext.lower())

    @staticmethod
    def is_sniffable_binary( filename ):
        format_information = None
        for format in Binary.sniffable_binary_formats:
            format_instance = format[ "class" ]()
            try:
                if format_instance.sniff(filename):
                    format_information = ( format["type"], format[ "ext" ] )
                    break
            except Exception:
                # Sniffer raised exception, could be any number of
                # reasons for this so there is not much to do besides
                # trying next sniffer.
                pass
        return format_information

    @staticmethod
    def is_ext_unsniffable(ext):
        return ext in Binary.unsniffable_binary_formats

    def set_peek( self, dataset, is_multi_byte=False ):
        """Set the peek and blurb text"""
        if not dataset.dataset.purged:
            dataset.peek = 'binary data'
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def get_mime( self ):
        """Returns the mime type of the datatype"""
        return 'application/octet-stream'

    def display_data(self, trans, dataset, preview=False, filename=None, to_ext=None, **kwd):
        trans.response.set_content_type(dataset.get_mime())
        trans.log_event( "Display dataset id: %s" % str( dataset.id ) )
        trans.response.headers['Content-Length'] = int( os.stat( dataset.file_name ).st_size )
        to_ext = dataset.extension
        fname = ''.join(c in FILENAME_VALID_CHARS and c or '_' for c in dataset.name)[0:150]
        trans.response.set_content_type( "application/octet-stream" )  # force octet-stream so Safari doesn't append mime extensions to filename
        trans.response.headers["Content-Disposition"] = 'attachment; filename="Galaxy%s-[%s].%s"' % (dataset.hid, fname, to_ext)
        return open( dataset.file_name )


class Ab1( Binary ):
    """Class describing an ab1 binary sequence file"""
    file_ext = "ab1"
    edam_format = "format_3000"
    edam_data = "data_0924"

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Binary ab1 sequence file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary ab1 sequence file (%s)" % ( nice_size( dataset.get_size() ) )


Binary.register_unsniffable_binary_ext("ab1")


class Idat( Binary ):
    """Binary data in idat format"""
    file_ext = "idat"
    edam_format = "format_2058"
    edam_data = "data_2603"

    def sniff( self, filename ):
        try:
            header = open( filename, 'rb' ).read(4)
            if header == b'IDAT':
                return True
            return False
        except:
            return False


Binary.register_sniffable_binary_format("idat", "idat", Idat)


class Cel( Binary ):

    """Binary data in CEL format."""
    file_ext = "cel"
    edam_format = "format_1638"
    edam_data = "data_3110"

    def sniff( self, filename ):
        """
        Try to guess if the file is a CEL file.

        >>> from galaxy.datatypes.sniff import get_test_fname
        >>> fname = get_test_fname('test.CEL')
        >>> Cel().sniff(fname)
        True

        >>> fname = get_test_fname('drugbank_drugs.mz5')
        >>> Cel().sniff(fname)
        False
        """
        try:
            header = open( filename, 'rb' ).read(4)
            if header == b';\x01\x00\x00':
                return True
            return False
        except:
            return False


Binary.register_sniffable_binary_format("cel", "cel", Cel)


class CompressedArchive( Binary ):
    """
        Class describing an compressed binary file
        This class can be sublass'ed to implement archive filetypes that will not be unpacked by upload.py.
    """
    file_ext = "compressed_archive"
    compressed = True

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Compressed binary file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Compressed binary file (%s)" % ( nice_size( dataset.get_size() ) )


Binary.register_unsniffable_binary_ext("compressed_archive")


class CompressedZipArchive( CompressedArchive ):
    """
        Class describing an compressed binary file
        This class can be sublass'ed to implement archive filetypes that will not be unpacked by upload.py.
    """
    file_ext = "zip"

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Compressed zip file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Compressed zip file (%s)" % ( nice_size( dataset.get_size() ) )


Binary.register_unsniffable_binary_ext("zip")


class GenericAsn1Binary( Binary ):
    """Class for generic ASN.1 binary format"""
    file_ext = "asn1-binary"
    edam_format = "format_1966"
    edam_data = "data_0849"


Binary.register_unsniffable_binary_ext("asn1-binary")


class CRAM( Binary ):
    file_ext = "cram"
    edam_format = "format_3462"
    edam_data = "format_0863"

    MetadataElement( name="cram_version", default=None, desc="CRAM Version", param=MetadataParameter, readonly=True, visible=False, optional=False, no_value=None )
    MetadataElement( name="cram_index", desc="CRAM Index File", param=metadata.FileParameter, file_ext="crai", readonly=True, no_value=None, visible=False, optional=True )

    def set_meta( self, dataset, overwrite=True, **kwd ):
        major_version, minor_version = self.get_cram_version( dataset.file_name )
        if major_version != -1:
            dataset.metadata.cram_version = str(major_version) + "." + str(minor_version)

        if not dataset.metadata.cram_index:
            index_file = dataset.metadata.spec['cram_index'].param.new_file( dataset=dataset )
            if self.set_index_file(dataset, index_file):
                dataset.metadata.cram_index = index_file

    def get_cram_version( self, filename):
        try:
            with open( filename, "rb") as fh:
                header = fh.read(6)
            return ord( header[4] ), ord( header[5] )
        except Exception as exc:
            log.warning( '%s, get_cram_version Exception: %s', self, exc )
            return -1, -1

    def set_index_file(self, dataset, index_file):
        try:
            # @todo when pysam 1.2.1 or pysam 1.3.0 gets released and becomes
            # a dependency of galaxy, use pysam.index(alignment, target_idx)
            # This currently gives coredump in the current release but is
            # fixed in the dev branch:
            # xref: https://github.com/samtools/samtools/issues/199

            dataset_symlink = os.path.join( os.path.dirname( index_file.file_name ), '__dataset_%d_%s' % ( dataset.id, os.path.basename( index_file.file_name ) ) )
            os.symlink( dataset.file_name, dataset_symlink )
            pysam.index( dataset_symlink )

            tmp_index = dataset_symlink + ".crai"
            if os.path.isfile( tmp_index ):
                shutil.move( tmp_index, index_file.file_name )
                return index_file.file_name
            else:
                os.unlink( dataset_symlink )
                log.warning( '%s, expected crai index not created for: %s', self, dataset.file_name )
                return False
        except Exception as exc:
            log.warning( '%s, set_index_file Exception: %s', self, exc )
            return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = 'CRAM binary alignment file'
            dataset.blurb = 'binary data'
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def sniff( self, filename ):
        try:
            header = open( filename, 'rb' ).read(4)
            if header == b"CRAM":
                return True
            return False
        except:
            return False


Binary.register_sniffable_binary_format('cram', 'cram', CRAM)


class Bcf( Binary):
    """Class describing a BCF file"""
    edam_format = "format_3020"
    edam_data = "data_3498"
    file_ext = "bcf"

    MetadataElement( name="bcf_index", desc="BCF Index File", param=metadata.FileParameter, file_ext="csi", readonly=True, no_value=None, visible=False, optional=True )

    def sniff( self, filename ):
        # BCF is compressed in the BGZF format, and must not be uncompressed in Galaxy.
        # The first 3 bytes of any bcf file is 'BCF', and the file is binary.
        try:
            header = gzip.open( filename ).read(3)
            if header == b'BCF':
                return True
            return False
        except:
            return False

    def set_meta( self, dataset, overwrite=True, **kwd ):
        """ Creates the index for the BCF file. """
        # These metadata values are not accessible by users, always overwrite
        index_file = dataset.metadata.bcf_index
        if not index_file:
            index_file = dataset.metadata.spec['bcf_index'].param.new_file( dataset=dataset )
        # Create the bcf index
        # $ bcftools index
        # Usage: bcftools index <in.bcf>

        dataset_symlink = os.path.join( os.path.dirname( index_file.file_name ),
                                        '__dataset_%d_%s' % ( dataset.id, os.path.basename( index_file.file_name ) ) )
        os.symlink( dataset.file_name, dataset_symlink )

        stderr_name = tempfile.NamedTemporaryFile( prefix="bcf_index_stderr" ).name
        command = [ 'bcftools', 'index', dataset_symlink ]
        try:
            subprocess.check_call( args=command, stderr=open( stderr_name, 'wb' ) )
            shutil.move( dataset_symlink + '.csi', index_file.file_name )  # this will fail if bcftools < 1.0 is used, because it creates a .bci index file instead of .csi
        except Exception as e:
            stderr = open( stderr_name ).read().strip()
            raise Exception('Error setting BCF metadata: %s' % (stderr or str(e)))
        finally:
            # Remove temp file and symlink
            os.remove( stderr_name )
            os.remove( dataset_symlink )
        dataset.metadata.bcf_index = index_file


Binary.register_sniffable_binary_format("bcf", "bcf", Bcf)


class H5( Binary ):
    """
    Class describing an HDF5 file

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'test.mz5' )
    >>> H5().sniff( fname )
    True
    >>> fname = get_test_fname( 'interval.interval' )
    >>> H5().sniff( fname )
    False
    """
    file_ext = "h5"
    edam_format = "format_3590"

    def __init__( self, **kwd ):
        Binary.__init__( self, **kwd )
        self._magic = binascii.unhexlify("894844460d0a1a0a")

    def sniff( self, filename ):
        # The first 8 bytes of any hdf5 file are 0x894844460d0a1a0a
        try:
            header = open( filename, 'rb' ).read(8)
            if header == self._magic:
                return True
            return False
        except:
            return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Binary HDF5 file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary HDF5 file (%s)" % ( nice_size( dataset.get_size() ) )


Binary.register_sniffable_binary_format("h5", "h5", H5)


class Scf( Binary ):
    """Class describing an scf binary sequence file"""
    edam_format = "format_1632"
    edam_data = "data_0924"
    file_ext = "scf"

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Binary scf sequence file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary scf sequence file (%s)" % ( nice_size( dataset.get_size() ) )


Binary.register_unsniffable_binary_ext("scf")


class Sff( Binary ):
    """ Standard Flowgram Format (SFF) """
    edam_format = "format_3284"
    edam_data = "data_0924"
    file_ext = "sff"

    def sniff( self, filename ):
        # The first 4 bytes of any sff file is '.sff', and the file is binary. For details
        # about the format, see http://www.ncbi.nlm.nih.gov/Traces/trace.cgi?cmd=show&f=formats&m=doc&s=format
        try:
            header = open( filename, 'rb' ).read(4)
            if header == b'.sff':
                return True
            return False
        except:
            return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Binary sff file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary sff file (%s)" % ( nice_size( dataset.get_size() ) )


Binary.register_sniffable_binary_format("sff", "sff", Sff)


class BigWig(Binary):
    """
    Accessing binary BigWig files from UCSC.
    The supplemental info in the paper has the binary details:
    http://bioinformatics.oxfordjournals.org/cgi/content/abstract/btq351v1
    """
    edam_format = "format_3006"
    edam_data = "data_3002"
    track_type = "LineTrack"
    data_sources = { "data_standalone": "bigwig" }

    def __init__( self, **kwd ):
        Binary.__init__( self, **kwd )
        self._magic = 0x888FFC26
        self._name = "BigWig"

    def _unpack( self, pattern, handle ):
        return struct.unpack( pattern, handle.read( struct.calcsize( pattern ) ) )

    def sniff( self, filename ):
        try:
            magic = self._unpack( "I", open( filename, 'rb' ) )
            return magic[0] == self._magic
        except:
            return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Binary UCSC %s file" % self._name
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary UCSC %s file (%s)" % ( self._name, nice_size( dataset.get_size() ) )


Binary.register_sniffable_binary_format("bigwig", "bigwig", BigWig)


class BigBed(BigWig):
    """BigBed support from UCSC."""
    edam_format = "format_3004"
    edam_data = "data_3002"
    data_sources = { "data_standalone": "bigbed" }

    def __init__( self, **kwd ):
        Binary.__init__( self, **kwd )
        self._magic = 0x8789F2EB
        self._name = "BigBed"


Binary.register_sniffable_binary_format("bigbed", "bigbed", BigBed)


class TwoBit (Binary):
    """Class describing a TwoBit format nucleotide file"""
    edam_format = "format_3009"
    edam_data = "data_0848"
    file_ext = "twobit"

    def sniff(self, filename):
        try:
            # All twobit files start with a 16-byte header. If the file is smaller than 16 bytes, it's obviously not a valid twobit file.
            if os.path.getsize(filename) < 16:
                return False
            header = open(filename, 'rb').read(TWOBIT_MAGIC_SIZE)
            magic = struct.unpack(">L", header)[0]
            if magic == TWOBIT_MAGIC_NUMBER or magic == TWOBIT_MAGIC_NUMBER_SWAP:
                return True
        except IOError:
            return False

    def set_peek(self, dataset, is_multi_byte=False):
        if not dataset.dataset.purged:
            dataset.peek = "Binary TwoBit format nucleotide file"
            dataset.blurb = nice_size(dataset.get_size())
        else:
            return super(TwoBit, self).set_peek(dataset, is_multi_byte)

    def display_peek(self, dataset):
        try:
            return dataset.peek
        except:
            return "Binary TwoBit format nucleotide file (%s)" % (nice_size(dataset.get_size()))


Binary.register_sniffable_binary_format("twobit", "twobit", TwoBit)


@dataproviders.decorators.has_dataproviders
class SQlite ( Binary ):
    """Class describing a Sqlite database """
    MetadataElement( name="tables", default=[], param=ListParameter, desc="Database Tables", readonly=True, visible=True, no_value=[] )
    MetadataElement( name="table_columns", default={}, param=DictParameter, desc="Database Table Columns", readonly=True, visible=True, no_value={} )
    MetadataElement( name="table_row_count", default={}, param=DictParameter, desc="Database Table Row Count", readonly=True, visible=True, no_value={} )
    file_ext = "sqlite"
    edam_format = "format_3621"

    def init_meta( self, dataset, copy_from=None ):
        Binary.init_meta( self, dataset, copy_from=copy_from )

    def set_meta( self, dataset, overwrite=True, **kwd ):
        try:
            tables = []
            columns = dict()
            rowcounts = dict()
            conn = sqlite.connect(dataset.file_name)
            c = conn.cursor()
            tables_query = "SELECT name,sql FROM sqlite_master WHERE type='table' ORDER BY name"
            rslt = c.execute(tables_query).fetchall()
            for table, sql in rslt:
                tables.append(table)
                try:
                    col_query = 'SELECT * FROM %s LIMIT 0' % table
                    cur = conn.cursor().execute(col_query)
                    cols = [col[0] for col in cur.description]
                    columns[table] = cols
                except Exception as exc:
                    log.warning( '%s, set_meta Exception: %s', self, exc )
            for table in tables:
                try:
                    row_query = "SELECT count(*) FROM %s" % table
                    rowcounts[table] = c.execute(row_query).fetchone()[0]
                except Exception as exc:
                    log.warning( '%s, set_meta Exception: %s', self, exc )
            dataset.metadata.tables = tables
            dataset.metadata.table_columns = columns
            dataset.metadata.table_row_count = rowcounts
        except Exception as exc:
            log.warning( '%s, set_meta Exception: %s', self, exc )

    def sniff( self, filename ):
        # The first 16 bytes of any SQLite3 database file is 'SQLite format 3\0', and the file is binary. For details
        # about the format, see http://www.sqlite.org/fileformat.html
        try:
            header = open(filename, 'rb').read(16)
            if header == b'SQLite format 3\0':
                return True
            return False
        except:
            return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "SQLite Database"
            lines = ['SQLite Database']
            if dataset.metadata.tables:
                for table in dataset.metadata.tables:
                    try:
                        lines.append('%s [%s]' % (table, dataset.metadata.table_row_count[table]))
                    except:
                        continue
            dataset.peek = '\n'.join(lines)
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "SQLite Database (%s)" % ( nice_size( dataset.get_size() ) )

    @dataproviders.decorators.dataprovider_factory( 'sqlite', dataproviders.dataset.SQliteDataProvider.settings )
    def sqlite_dataprovider( self, dataset, **settings ):
        dataset_source = dataproviders.dataset.DatasetDataProvider( dataset )
        return dataproviders.dataset.SQliteDataProvider( dataset_source, **settings )

    @dataproviders.decorators.dataprovider_factory( 'sqlite-table', dataproviders.dataset.SQliteDataTableProvider.settings )
    def sqlite_datatableprovider( self, dataset, **settings ):
        dataset_source = dataproviders.dataset.DatasetDataProvider( dataset )
        return dataproviders.dataset.SQliteDataTableProvider( dataset_source, **settings )

    @dataproviders.decorators.dataprovider_factory( 'sqlite-dict', dataproviders.dataset.SQliteDataDictProvider.settings )
    def sqlite_datadictprovider( self, dataset, **settings ):
        dataset_source = dataproviders.dataset.DatasetDataProvider( dataset )
        return dataproviders.dataset.SQliteDataDictProvider( dataset_source, **settings )


# Binary.register_sniffable_binary_format("sqlite", "sqlite", SQlite)


class GeminiSQLite( SQlite ):
    """Class describing a Gemini Sqlite database """
    MetadataElement( name="gemini_version", default='0.10.0', param=MetadataParameter, desc="Gemini Version",
                     readonly=True, visible=True, no_value='0.10.0' )
    file_ext = "gemini.sqlite"
    edam_format = "format_3622"
    edam_data = "data_3498"

    def set_meta( self, dataset, overwrite=True, **kwd ):
        super( GeminiSQLite, self ).set_meta( dataset, overwrite=overwrite, **kwd )
        try:
            conn = sqlite.connect( dataset.file_name )
            c = conn.cursor()
            tables_query = "SELECT version FROM version"
            result = c.execute( tables_query ).fetchall()
            for version, in result:
                dataset.metadata.gemini_version = version
            # TODO: Can/should we detect even more attributes, such as use of PED file, what was input annotation type, etc.
        except Exception as e:
            log.warning( '%s, set_meta Exception: %s', self, e )

    def sniff( self, filename ):
        if super( GeminiSQLite, self ).sniff( filename ):
            gemini_table_names = [ "gene_detailed", "gene_summary", "resources", "sample_genotype_counts", "sample_genotypes", "samples",
                                   "variant_impacts", "variants", "version" ]
            try:
                conn = sqlite.connect( filename )
                c = conn.cursor()
                tables_query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
                result = c.execute( tables_query ).fetchall()
                result = [_[0] for _ in result]
                for table_name in gemini_table_names:
                    if table_name not in result:
                        return False
                return True
            except Exception as e:
                log.warning( '%s, sniff Exception: %s', self, e )
        return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Gemini SQLite Database, version %s" % ( dataset.metadata.gemini_version or 'unknown' )
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Gemini SQLite Database, version %s" % ( dataset.metadata.gemini_version or 'unknown' )


class MzSQlite( SQlite ):
    """Class describing a Proteomics Sqlite database """
    file_ext = "mz.sqlite"

    def set_meta( self, dataset, overwrite=True, **kwd ):
        super( MzSQlite, self ).set_meta( dataset, overwrite=overwrite, **kwd )

    def sniff( self, filename ):
        if super( MzSQlite, self ).sniff( filename ):
            mz_table_names = ["DBSequence", "Modification", "Peaks", "Peptide", "PeptideEvidence", "Score", "SearchDatabase", "Source", "SpectraData", "Spectrum", "SpectrumIdentification"]
            try:
                conn = sqlite.connect( filename )
                c = conn.cursor()
                tables_query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
                result = c.execute( tables_query ).fetchall()
                result = [_[0] for _ in result]
                for table_name in mz_table_names:
                    if table_name not in result:
                        return False
                return True
            except Exception as e:
                log.warning( '%s, sniff Exception: %s', self, e )
        return False


class IdpDB( SQlite ):
    """
    Class describing an IDPicker 3 idpDB (sqlite) database

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'test.idpDB' )
    >>> IdpDB().sniff( fname )
    True
    >>> fname = get_test_fname( 'interval.interval' )
    >>> IdpDB().sniff( fname )
    False
    """
    file_ext = "idpdb"

    def set_meta( self, dataset, overwrite=True, **kwd ):
        super( IdpDB, self ).set_meta( dataset, overwrite=overwrite, **kwd )

    def sniff( self, filename ):
        if super( IdpDB, self ).sniff( filename ):
            mz_table_names = ["About", "Analysis", "AnalysisParameter", "PeptideSpectrumMatch", "Spectrum", "SpectrumSource"]
            try:
                conn = sqlite.connect( filename )
                c = conn.cursor()
                tables_query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
                result = c.execute( tables_query ).fetchall()
                result = [_[0] for _ in result]
                for table_name in mz_table_names:
                    if table_name not in result:
                        return False
                return True
            except Exception as e:
                log.warning( '%s, sniff Exception: %s', self, e )
        return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "IDPickerDB SQLite file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "IDPickerDB SQLite file (%s)" % ( nice_size( dataset.get_size() ) )


Binary.register_sniffable_binary_format( "gemini.sqlite", "gemini.sqlite", GeminiSQLite )
Binary.register_sniffable_binary_format( "idpdb", "idpdb", IdpDB )
Binary.register_sniffable_binary_format( "mz.sqlite", "mz.sqlite", MzSQlite )
# FIXME: We need to register specialized sqlite formats before sqlite, since register_sniffable_binary_format and is_sniffable_binary called in upload.py
# ignores sniff order declared in datatypes_conf.xml
Binary.register_sniffable_binary_format("sqlite", "sqlite", SQlite)


class Xlsx(Binary):
    """Class for Excel 2007 (xlsx) files"""
    file_ext = "xlsx"

    def sniff( self, filename ):
        # Xlsx is compressed in zip format and must not be uncompressed in Galaxy.
        try:
            if zipfile.is_zipfile( filename ):
                tempzip = zipfile.ZipFile( filename )
                if "[Content_Types].xml" in tempzip.namelist() and tempzip.read("[Content_Types].xml").find(b'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml') != -1:
                    return True
            return False
        except:
            return False


Binary.register_sniffable_binary_format("xlsx", "xlsx", Xlsx)


class Sra( Binary ):
    """ Sequence Read Archive (SRA) datatype originally from mdshw5/sra-tools-galaxy"""
    file_ext = 'sra'

    def sniff( self, filename ):
        """ The first 8 bytes of any NCBI sra file is 'NCBI.sra', and the file is binary.
        For details about the format, see http://www.ncbi.nlm.nih.gov/books/n/helpsra/SRA_Overview_BK/#SRA_Overview_BK.4_SRA_Data_Structure
        """
        try:
            header = open(filename, 'rb').read(8)
            if header == b'NCBI.sra':
                return True
            else:
                return False
        except:
            return False

    def set_peek(self, dataset, is_multi_byte=False):
        if not dataset.dataset.purged:
            dataset.peek = 'Binary sra file'
            dataset.blurb = nice_size(dataset.get_size())
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek(self, dataset):
        try:
            return dataset.peek
        except:
            return 'Binary sra file (%s)' % (nice_size(dataset.get_size()))


Binary.register_sniffable_binary_format('sra', 'sra', Sra)


class RData( Binary ):
    """Generic R Data file datatype implementation"""
    file_ext = 'RData'

    def sniff( self, filename ):
        rdata_header = b'RDX2\nX\n'
        try:
            header = open(filename, 'rb').read(7)
            if header == rdata_header:
                return True

            header = gzip.open( filename ).read(7)
            if header == rdata_header:
                return True
        except:
            return False


Binary.register_sniffable_binary_format('RData', 'RData', RData)


class OxliBinary(Binary):

    @staticmethod
    def _sniff(filename, oxlitype):
        try:
            with open(filename, 'rb') as fileobj:
                header = fileobj.read(4)
                if header == b'OXLI':
                    fileobj.read(1)  # skip the version number
                    ftype = fileobj.read(1)
                    if binascii.hexlify(ftype) == oxlitype:
                        return True
            return False
        except IOError:
            return False


class OxliCountGraph(OxliBinary):
    """
    OxliCountGraph starts with "OXLI" + one byte version number +
    8-bit binary '1'
    Test file generated via::

        load-into-counting.py --n_tables 1 --max-tablesize 1 \\
            oxli_countgraph.oxlicg khmer/tests/test-data/100-reads.fq.bz2

    using khmer 2.0

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'sequence.csfasta' )
    >>> OxliCountGraph().sniff( fname )
    False
    >>> fname = get_test_fname( "oxli_countgraph.oxlicg" )
    >>> OxliCountGraph().sniff( fname )
    True
    """

    def sniff(self, filename):
        return OxliBinary._sniff(filename, b"01")


Binary.register_sniffable_binary_format("oxli.countgraph", "oxlicg",
                                        OxliCountGraph)


class OxliNodeGraph(OxliBinary):
    """
    OxliNodeGraph starts with "OXLI" + one byte version number +
    8-bit binary '2'
    Test file generated via::

        load-graph.py --n_tables 1 --max-tablesize 1 oxli_nodegraph.oxling \\
            khmer/tests/test-data/100-reads.fq.bz2

    using khmer 2.0

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'sequence.csfasta' )
    >>> OxliNodeGraph().sniff( fname )
    False
    >>> fname = get_test_fname( "oxli_nodegraph.oxling" )
    >>> OxliNodeGraph().sniff( fname )
    True
    """

    def sniff(self, filename):
        return OxliBinary._sniff(filename, b"02")


Binary.register_sniffable_binary_format("oxli.nodegraph", "oxling",
                                        OxliNodeGraph)


class OxliTagSet(OxliBinary):
    """
    OxliTagSet starts with "OXLI" + one byte version number +
    8-bit binary '3'
    Test file generated via::

        load-graph.py --n_tables 1 --max-tablesize 1 oxli_nodegraph.oxling \\
            khmer/tests/test-data/100-reads.fq.bz2;
        mv oxli_nodegraph.oxling.tagset oxli_tagset.oxlits

    using khmer 2.0

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'sequence.csfasta' )
    >>> OxliTagSet().sniff( fname )
    False
    >>> fname = get_test_fname( "oxli_tagset.oxlits" )
    >>> OxliTagSet().sniff( fname )
    True
    """

    def sniff(self, filename):
        return OxliBinary._sniff(filename, b"03")


Binary.register_sniffable_binary_format("oxli.tagset", "oxlits", OxliTagSet)


class OxliStopTags(OxliBinary):
    """
    OxliStopTags starts with "OXLI" + one byte version number +
    8-bit binary '4'
    Test file adapted from khmer 2.0's
    "khmer/tests/test-data/goodversion-k32.stoptags"

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'sequence.csfasta' )
    >>> OxliStopTags().sniff( fname )
    False
    >>> fname = get_test_fname( "oxli_stoptags.oxlist" )
    >>> OxliStopTags().sniff( fname )
    True
    """

    def sniff(self, filename):
        return OxliBinary._sniff(filename, b"04")


Binary.register_sniffable_binary_format("oxli.stoptags", "oxlist",
                                        OxliStopTags)


class OxliSubset(OxliBinary):
    """
    OxliSubset starts with "OXLI" + one byte version number +
    8-bit binary '5'
    Test file generated via::

        load-graph.py -k 20 example tests/test-data/random-20-a.fa;
        partition-graph.py example;
        mv example.subset.0.pmap oxli_subset.oxliss

    using khmer 2.0

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'sequence.csfasta' )
    >>> OxliSubset().sniff( fname )
    False
    >>> fname = get_test_fname( "oxli_subset.oxliss" )
    >>> OxliSubset().sniff( fname )
    True
    """

    def sniff(self, filename):
        return OxliBinary._sniff(filename, b"05")


Binary.register_sniffable_binary_format("oxli.subset", "oxliss", OxliSubset)


class OxliGraphLabels(OxliBinary):
    """
    OxliGraphLabels starts with "OXLI" + one byte version number +
    8-bit binary '6'
    Test file generated via::

        python -c "from khmer import GraphLabels; \\
            gl = GraphLabels(20, 1e7, 4); \\
            gl.consume_fasta_and_tag_with_labels('tests/test-data/test-labels.fa'); \\
            gl.save_labels_and_tags('oxli_graphlabels.oxligl')"

    using khmer 2.0

    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'sequence.csfasta' )
    >>> OxliGraphLabels().sniff( fname )
    False
    >>> fname = get_test_fname( "oxli_graphlabels.oxligl" )
    >>> OxliGraphLabels().sniff( fname )
    True
    """

    def sniff(self, filename):
        return OxliBinary._sniff(filename, b"06")


Binary.register_sniffable_binary_format("oxli.graphlabels", "oxligl",
                                        OxliGraphLabels)


class SearchGuiArchive ( CompressedArchive ):
    """Class describing a SearchGUI archive """
    MetadataElement( name="searchgui_version", default='1.28.0', param=MetadataParameter, desc="SearchGui Version",
                     readonly=True, visible=True, no_value=None )
    MetadataElement( name="searchgui_major_version", default='1', param=MetadataParameter, desc="SearchGui Major Version",
                     readonly=True, visible=True, no_value=None )
    file_ext = "searchgui_archive"

    def set_meta( self, dataset, overwrite=True, **kwd ):
        super( SearchGuiArchive, self ).set_meta( dataset, overwrite=overwrite, **kwd )
        try:
            if dataset and zipfile.is_zipfile( dataset.file_name ):
                tempzip = zipfile.ZipFile( dataset.file_name )
                if 'searchgui.properties' in tempzip.namelist():
                    fh = tempzip.open('searchgui.properties')
                    for line in fh:
                        if line.startswith('searchgui.version'):
                            version = line.split('=')[1].strip()
                            dataset.metadata.searchgui_version = version
                            dataset.metadata.searchgui_major_version = version.split('.')[0]
                    fh.close()
                tempzip.close()
        except Exception as e:
            log.warning( '%s, set_meta Exception: %s', self, e )

    def sniff( self, filename ):
        try:
            if filename and zipfile.is_zipfile( filename ):
                tempzip = zipfile.ZipFile( filename, 'r' )
                is_searchgui = 'searchgui.properties' in tempzip.namelist()
                tempzip.close()
                return is_searchgui
        except Exception as e:
            log.warning( '%s, sniff Exception: %s', self, e )
        return False

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "SearchGUI Archive, version %s" % ( dataset.metadata.searchgui_version or 'unknown' )
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "SearchGUI Archive, version %s" % ( dataset.metadata.searchgui_version or 'unknown' )


Binary.register_sniffable_binary_format("searchgui_archive", "searchgui_archive", SearchGuiArchive)


class NetCDF( Binary ):
    """Binary data in netCDF format"""
    file_ext = "netcdf"
    edam_format = "format_3650"
    edam_data = "data_0943"

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek = "Binary netCDF file"
            dataset.blurb = nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary netCDF file (%s)" % ( nice_size( dataset.get_size() ) )

    def sniff( self, filename ):
        try:
            with open( filename, 'rb' ) as f:
                header = f.read(3)
            if header == b'CDF':
                return True
            return False
        except:
            return False


Binary.register_sniffable_binary_format("netcdf", "netcdf", NetCDF)


class DMND( Binary ):
    """
    Class describing an DMND file
    >>> from galaxy.datatypes.sniff import get_test_fname
    >>> fname = get_test_fname( 'diamond_db.dmnd' )
    >>> DMND().sniff( fname )
    True
    >>> fname = get_test_fname( 'interval.interval' )
    >>> DMND().sniff( fname )
    False
    """
    file_ext = "dmnd"
    edam_format = ""

    def __init__( self, **kwd ):
        Binary.__init__( self, **kwd )
        self._magic = binascii.unhexlify("6d18ee15a4f84a02")

    def sniff( self, filename ):
        # The first 8 bytes of any dmnd file are 0x24af8a415ee186d

        try:
            header = open( filename, 'rb' ).read(8)
            if header == self._magic:
                return True
            return False
        except:
            return False


Binary.register_sniffable_binary_format("dmnd", "dmnd", DMND)
