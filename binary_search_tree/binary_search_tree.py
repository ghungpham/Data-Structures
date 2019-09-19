#import sys
#sys.path.append('../queue_and_stack')
#from dll_queue import Queue
#from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if self.value > new_node.value:
      if self.left == None:
        self.left = new_node
      else:
        self.left.insert(value)
    if self.value < new_node.value:
      if self.right == None:
        self.right = new_node
      else:
        self.right.insert(value)

    

  def contains(self, target):
    if self.value == target:
      return True
    if self.value > target:
      if not self.left:
        return False
      return self.left.contains(target)
    else:
      if not self.right:
        return False
      return self.right.contains(target)


  def get_max(self):
    if not self.right:
      return self.value
    while self.right:
      max_value = self.right.value
      self.right = self.right.right
    return max_value
##### if not self.right: return self.value return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

    

