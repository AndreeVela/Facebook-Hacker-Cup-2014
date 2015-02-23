class Node(object) :
	char = ''
	ends = False
	parent = None
	child = None

	def __init__( self, char, parent ) :
		self.char = char
		self.parent = parent
		self.child = [None]*26

	def get_child( self, char ) :
		return self.child[ ord( char ) - 97 ] if ord( char ) - 97 > 0 else None

	def add_child( self, node ) :
		self.child[ ord( node.char ) - 97 ] = node

	def get_deep( self ) :
		if self.parent == None : return 0
		else : return self.parent.get_deep() + 1

	def is_unambiguous( self, no_end ):
		result = True

		if self.ends and !no_end :
			return true

		# soy final de palabra y hay mas cosas adelante
			# soy inanbiguo si el de adelante lo es
		# no soy final de palabra y hay mas cosas adelante


	# 	return !self.ends and

	def have_childs( self ) :
		for node in self.child :
			if node != None : return True
		else :
			return False

	def __str__( self ):
		desc = 'Char: ' + self.char + ' Parent: ' + self.parent.char +  ' Childs: [ '
		for node in self.child :
			if node != None :
				desc += node.char + ', '
		return desc + ']'


class Trie :
	root = Node( '\x00', None )

	def insert( self, word ):
		current = self.root

		for i in range( len( word ) ) :
			sub = current.get_child( word[i] )

			if sub != None :
				current = sub
			else :
				new = Node( word[i], current )
				current.add_child( new )
				current = current.get_child( word[i] )

			current.ends = True if (len( word )-1 == i) else False

	def search( self, word, keys=1 ) :
		current = self.root

		for i in range( len( word ) ) :
			current = current.get_child( word[i] )

			if current == None:
				self.insert( word )
				return keys
			else : # verificar si la letra es ambigua


			keys += 1
		return keys

if __name__ == "__main__":
	content = map( lambda s: s.strip(), open( 'autocomplete_example_input.txt', 'r' ).readlines() )
	n_tests = int( content[0] )
	del content[0]

	trie = Trie()

	for i in range( n_tests ) :
		n_words = int( content[0] )

		for k in range( n_words ) :
			trie.search( content[k] )
			# trie.insert( content[k+1] )

		content = content[int(n_words)+1:]

