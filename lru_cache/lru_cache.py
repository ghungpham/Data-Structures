from doubly_linked_list import DoublyLinkedList
class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit #max of how many nodes it can carry
    self.size = 0 #length
    self.order = DoublyLinkedList()
    self.storage = dict()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    #pull the dict out of the dictionary
    if key in self.storage:
      node = self.storage[key]
      self.order.move_to_front(node)
      return node.value[1]
    else:
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    #Add  a pair to the cache
    if key in self.storage:
      node = self.storage[key]
      node.value = (key, value) ##tying the tuple to the order
      self.order.move_to_front(node)
      return
    #newly added pair most recently used
    #oldest entry in the cache needs to be removed
    if self.size == self.limit:
      del self.storage[self.order.tail.value[0]] # remove from the dict
      self.order.remove_from_tail() # remove from the linked list
      self.size -= 1
    
    self.order.add_to_head((key, value))
    self.storage[key] = self.order.head
    self.size += 1 



    #if the key already exists, overwrite old value, with new
  
