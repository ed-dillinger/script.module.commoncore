# -*- coding: utf-8 -*-

'''*
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
*'''

import hashlib
import pyaes
import base64

class AESCipher(object):

	def __init__(self, key): 
		key = hashlib.md5(key).hexdigest()
		self.aes = pyaes.AESModeOfOperationCTR(key)
	
	def decrypt(self, strong):
		return self.aes.decrypt(strong)

	def encrypt(self, raw):
		return self.aes.encrypt(raw)
	
	def test_key(self):
		return self.decrypt(base64.b64decode('uGQsrQ==')) == 'True'
