from django.db import models
from django.contrib.auth.models import User

class Node(models.Model):
 #Content Information
 name = models.CharField(max_length=100, unique=True)
 content = models.CharField(max_length=2000)
 user = models.ForeignKey(User)

 #Rating Information
 good = models.IntegerField(default=0)
 bad = models.IntegerField(default=0)

 def __unicode__(self):
  return self.name

class Edge(models.Model):
 node1 = models.ForeignKey(Node, related_name="node1")
 node2 = models.ForeignKey(Node, related_name="node2")
 good = models.IntegerField(default=0)
 bad = models.IntegerField(default=0)
 hits = models.IntegerField(default = 0)

 def __unicode__(self):
  return "{} -- {}".format(self.node1, self.node2)

class Career(models.Model):
 name = models.CharField(max_length=100, unique=True)
 description = models.CharField(max_length=2000)
 user = models.ForeignKey(User)
 start_node = models.ForeignKey(Node)
 hits = models.IntegerField(default = 0)

 def __unicode__(self):
  return self.name


class CareerNodeMap(models.Model):
 node = models.ForeignKey(Node)
 career = models.ForeignKey(Career)
 user = models.ForeignKey(User)

class CareerEdgeMap(models.Model):
 edge = models.ForeignKey(Edge)
 career = models.ForeignKey(Career)
 user = models.ForeignKey(User)

class Link(models.Model):
 url = models.CharField(max_length=300, unique=True)
 hits = models.IntegerField(default = 0)
 good = models.IntegerField(default=0)
 bad = models.IntegerField(default=0)

 def __unicode__(self):
  return self.url


