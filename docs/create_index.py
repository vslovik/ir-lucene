import lucene
import sys
from lucene import *

lucene.initVM()  # Init JVM
dir_name = "test_index"
index_dir = SimpleFSDirectory(File(dir_name))  # Directory on file system to store index
analyzer = WhitespaceAnalyzer(Version.LUCENE_35)  # Create analyzer
writer = IndexWriter(index_dir, analyzer, True,
                     IndexWriter.MaxFieldLength.UNLIMITED)  # Create new index (delete any pre-existing data)

for l in sys.stdin:
        doc = Document()
        # Field.Store.YES - write the whole text (in original form) in the index
        # Field.Index.ANALYZED - use analyzer
        text_field = Field("text", l.strip(), Field.Store.YES, Field.Index.ANALYZED)
        doc.add(text_field)
        writer.addDocument(doc)
        print "Currently there are {0} documents in the index...".format(writer.numDocs())
writer.optimize()
writer.close()
