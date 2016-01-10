import lucene
import sys
from lucene import *

if __name__ == "__main__":
	lucene.initVM()
	dir_name = "test_index"
	index_dir = SimpleFSDirectory(File(dir_name))
	analyzer = ClassicAnalyzer(Version.LUCENE_35)
	writer = IndexWriter(index_dir, analyzer, True, IndexWriter.MaxFieldLength.UNLIMITED)
	
	for l in sys.stdin:
		doc = Document()
		text_field = Field("text", l.strip(), Field.Store.YES, Field.Index.ANALYZED)
		doc.add(text_field)
		writer.addDocument(doc)
		print "Currently there are {0} documents in the index...".format(writer.numDocs())
	
	writer.optimize()
	writer.close()
