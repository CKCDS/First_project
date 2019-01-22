# -*- coding: utf-8 -*-
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         # 数据库以及显示的字段
#         model = Snippet
#         fields = ('id', 'title', 'code', 'owner')
import re

f = open("models.py")
str = f.read()
f.close()
a = re.findall(r'class (.*?)\(models.Model\):', str)

str_1 = ''
for i in a:

    # str = re.sub(r'class {}\(models.Model\):'.format(i), 'class {}(models.Model):\n    id = models.CharField(max_length=100, primary_key=True)\n    '
    #                                                'def __init__(self, *args, **kwargs):\n        '
    #                                                'super({}, self).__init__(*args, **kwargs)\n'
    #                                                '        if not self.id:\n'
    #                                            '                self.id = uuid.uuid1()\n'.format(i,i), str, count=0, flags=0)
    # str_1 += "class {}List(generics.ListCreateAPIView):\n".format(i)
    # str_1 += "    queryset =  {}.objects.all()\n".format(i)
    # str_1 += "    serializer_class = {}Serializer\n".format(i)
    # str_1 += "    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)\n"
    # str_1 += "    filter_fields = '__all__'\n"
    # str_1 += "class {}Detail(generics.RetrieveUpdateDestroyAPIView):\n".format(i)
    # str_1 += "    queryset =  {}.objects.all()\n".format(i)
    # str_1 += "    serializer_class = {}Serializer\n".format(i)
    # str_1 += "    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)\n"
    # str_1 = "class {}ViewSet(viewsets.ReadOnlyModelViewSet):\n".format(i)
    # str_1 += "    queryset =  {}.objects.all()\n".format(i)
    # str_1 += "    serializer_class = {}Serializer\n".format(i)
    # str_1 += "    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)\n"

    # str_1+="router.register(r'{}', {}ViewSet)\n".format(i.lower(),i)
    # str_1 += 'url(r"^{}/$",{}List.as_view()),\n'.format(i.lower(),i)
    # str_1+= 'url(r"^{}/(?P<pk>[0-9]+)/$", {}Detail.as_view()),\n'.format(i.lower(),i)
    # str = re.sub(r'class {}\(serializers.ModelSerializer\):'.format(i),'class {}(serializers.ModelSerializer):\n    '
    #                                                                    'id = serializers.ReadOnlyField()\n'.format(i),str)
# str = re.sub(r"list_display = \(",'list_display = ("id",',str)
    s = i+"\n"
    str_1+=s
f = open("01.py", "a")
f.write(str_1)
f.close()
