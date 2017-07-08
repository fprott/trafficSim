from mathe import *
import math
import parameter




class Graph():
    """To generate a tree stucture"""
    def __init__(self):

        pass



class Node():
    def __init__(self,point,street,direction):
        #point = [x,y]
        #street are given with all nodes inside
        self.visited = 0
        self.positon = point
        self.street = street
        self.direction = direction
        self.upper_node = self.get_upper_node()
        self.lower_node = self.get_lower_node()
        pass

    def set_visited(self):
        self.visited = 1

    def get_upper_node(self):
        #TODO
        upper_node = []
        for i in range(len(self.street)):
            for j in range(1,len(self.street[i])-1):
                if self.street[i][j] == self.positon:
                    upper_node.append(self.street[i][j])

        return upper_node


    def get_lower_node(self):

        lower_node = []
        """
        for i in range(len(self.street)):
            if self.direction:
                for j in range(1,len(self.street[i])-1):
                    if self.street[i][j] == self.positon:
                        lower_node.append(self.street[i][j+1])
            else:
                for j in range(1,len(self.street[i]-1)):
                    if self.street[i][j] == self.positon:
                        lower_node.append(self.street[i][j-1])
        """

        for i in range(len(self.street)):
            for j in range(1,len(self.street[i])-1):
                if (self.street[i][j] == self.positon) or (self.street[i][j] == self.positon + [1]):
                    if (type(self.street[i][j-1])==type([])):
                        #& (self.street[i][j-1] != former_node):  make sure the element is a POSITION, not a WIDTH
                        lower_node.append(self.street[i][j-1])
                    #if self.street[i][j+1] != former_node: # make sure the former node not in the list
                    lower_node.append(self.street[i][j+1])




        return lower_node






class Path():
    def __init__(self,start,end,street):
        """start/end=[x,y]"""
        self.start = start
        self.end = end
        self.street = street
        self.direction = self.get_direction()
        pass

    def get_direction(self):
        #TODO
        if 1:
            direction = 1
        else:
            direction = 0

        return direction

    """
    def get_unvisited_child(self,node,all_visited,stack):

        ans =[]
        Node1 = Node(node,self.street,self.direction)
        a = Node1.get_lower_node()
        visited = list_and_list(a,all_visited)
        former_node = list_and_list(a,stack)
        need_to_remove = visited + former_node
        #find the visited nodes in the right layer
        if a == []:
            ans = []
        else:
            child = list_remove_list(a,need_to_remove)
            if child == []:
                ans = []
            else:
                ans = child[0]

        #ans = list_remove_list(ans,list_and_list(ans,stack))

        return ans
    """

    def get_unvisited_child(self,pos,stack):
        # unvisited可以直接从street里面读出
        ans =[]

        if len(pos) == 2:
            pos = pos + [1]


        Node1 = Node(pos,self.street,self.direction)
        all_child = Node1.get_lower_node()

        #print(all_child)

        child_without_stack = list_remove_list(all_child,list_and_list(all_child,stack))

        #print(list_and_list(all_child,stack))
        #print("child without stack")
        #print(child_without_stack)

        for i in range(len(child_without_stack)):

            if len(child_without_stack[i]) == 2:
                ans = child_without_stack[i]
                return ans
            """
            if not self.check_visited(child_without_stack[i]):
                ans = child_without_stack[i]
                return ans
            """

        return ans





    def depthFirstSearch_test(self):
        """Strassen_Nets = [
            [20, [0, 250], [250, 250], [400, 250]],
            [20, [250, 0], [250, 250], [250, 400]]
        ]"""

        """start=[0,250]
        end=[250,400]"""
        ans = []

        stack = []
        visited = []
        #print(self.start)
        startNode = Node(self.start,self.street,self.direction)
        stack.append(startNode.positon)
        #start.set_visited()


        #print(startNode.positon)
        print("A")
        print(visited)
        print(stack)
        pos = stack[len(stack)-1]
        node = Node(pos,self.street,self.direction)
        # *********NODE A**********
        if node.positon == self.end:
            # return stack
            ans.append(stack)
            e = stack.pop()
            visited.append(e)
        else:
            child = self.get_unvisited_child(node.positon, visited)  # list_remove_list(node.get_lower_node(),visited)
            if child == []:
                e = stack.pop()
                visited.append(e)
                last_node = Node(e, self.street, self.direction)
                lower_nodes = last_node.get_lower_node()
                visited = list_remove_list(visited, lower_nodes)
            else:
                child_node = Node(child, self.street, self.direction)
                print(child)
                #print(child_node.positon)
                stack.append(child_node.positon)

        print("B")
        print(visited)
        print(stack)
        pos = stack[len(stack) - 1]
        node = Node(pos, self.street, self.direction)
        # *********NODE B**********
        if node.positon == self.end:
            # return stack
            ans.append(stack)
            e = stack.pop()
            visited.append(e)
        else:
            child = self.get_unvisited_child(node.positon, visited)  # list_remove_list(node.get_lower_node(),visited)
            if child == []:
                #print(stack)
                e = stack.pop()
                #print(e)
                visited.append(e)
                last_node = Node(e, self.street, self.direction)
                lower_nodes = last_node.get_lower_node()
                visited = list_remove_list(visited, lower_nodes)
            else:
                child_node = Node(child, self.street, self.direction)
                stack.append(child_node.positon)

        print("C")
        print(visited)
        print(stack)
        pos = stack[len(stack) - 1]
        node = Node(pos, self.street, self.direction)
        # *********NODE C**********
        if node.positon == self.end:
            # return stack
            print("got an answer:")
            print(stack)
            ans.append(stack)
            e = stack.pop()
            visited.append(e)
        else:
            child = self.get_unvisited_child(node.positon, visited)  # list_remove_list(node.get_lower_node(),visited)
            if child == []:
                e = stack.pop()
                visited.append(e)
                last_node = Node(e, self.street, self.direction)
                lower_nodes = last_node.get_lower_node()
                visited = list_remove_list(visited, lower_nodes)
            else:
                child_node = Node(child, self.street, self.direction)
                stack.append(child_node.positon)

        print("E")
        print(stack)
        print(visited)
        pos = stack[len(stack) - 1]
        node = Node(pos, self.street, self.direction)
        # *********NODE E**********
        if node.positon == self.end:
            # return stack
            ans.append(stack)
            e = stack.pop()
            visited.append(e)
        else:
            child = self.get_unvisited_child(node.positon, visited)  # list_remove_list(node.get_lower_node(),visited)
            if child == []:
                e = stack.pop()
                visited.append(e)
                last_node = Node(e, self.street, self.direction)
                lower_nodes = last_node.get_lower_node()
                print("lower_nodes:")
                print(lower_nodes)
                visited = list_remove_list(visited, lower_nodes)
            else:
                child_node = Node(child, self.street, self.direction)
                stack.append(child_node.positon)

        print(stack)
        print(visited)
        print("After finished all nodes:")

        pos = stack[len(stack)-1]  #get the latest node in STACK
        node = Node(pos,self.street,self.direction)
        print("current Node:")
        print(node.positon)
        if node.positon == self.end:
            #return stack
            ans.append(stack)
            e = stack.pop()
            visited.append(e)
        else:
            print(visited)
            print(node.positon)
            #TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #Problem here: "visited" includes Node C, but the children of E is empty
            #Solution: changed the get_unvisited_child, when children is empty, just return directly []
            child = self.get_unvisited_child(node.positon,visited) #list_remove_list(node.get_lower_node(),visited)
            if child == []:
                e = stack.pop()
                visited.append(e)
                last_node = Node(e,self.street,self.direction)
                lower_nodes = last_node.get_lower_node()
                visited = list_remove_list(visited,lower_nodes)
            else:
                child_node = Node(child,self.street,self.direction)
                stack.append(child_node.positon)
                #node.set_visited()

        return ans





    def set_visited(self,node):

        a = list(node)

        for i in range(len(self.street)):
            for j in range(len(self.street[i])):
                if self.street[i][j] == a:
                    if len(self.street[i][j]) == 2:
                        self.street[i][j].append(1)


    def set_unvisited(self,node):

        #print(node)
        if len(node) == 2:
            a = node + [1]
        elif len(node) == 3:
            a = node

        #print(a)
        for i in range(len(self.street)):
            for j in range(len(self.street[i])):
                if self.street[i][j] == a:
                    if len(self.street[i][j]) == 3:
                        self.street[i][j].pop()


    def check_visited(self,pos):

        a = pos + [1]

        for i in range(len(self.street)):
            for j in range(len(self.street[i])):
                if self.street[i][j] == pos:
                    return 0

        for i in range(len(self.street)):
            for j in range(len(self.street[i])):
                if self.street[i][j] == a:
                    return 1



    def clear_visited(self,pos,stack):
        # pos点的所有child，除去stack里面的，(以及stack的child!!!!!!!!!!!!!),全部set_unvisited
        # stack里面的点都是visited
        Node1 = Node(pos,self.street,self.direction)
        all_child = Node1.get_lower_node()
        need_to_set = list_remove_list(all_child, list_and_list(all_child, stack))

        for j in range(len(stack)-1):
            Node_stack = Node(stack[j],self.street,self.direction)
            stack_child = Node_stack.get_lower_node()
            need_to_set = list_remove_list(need_to_set,list_and_list(need_to_set,stack_child))


        for i in range(len(need_to_set)-1):
            self.set_unvisited(need_to_set[i])



    def depthFirstSearch(self):
        """start/end=[x,y]"""
        ans = []

        stack = []
        visited = []
        startNode = Node(self.start,self.street,self.direction)
        stack.append(startNode.positon)
        self.set_visited(startNode.positon)

        while stack != []:
            pos = stack[len(stack)-1]  #get the latest node in STACK
            node = Node(pos,self.street,self.direction)
            if node.positon == (self.end + [1]):
                path = tuple(stack)
                #此处stack堆栈不能直接保存
                ans = ans + [path]
                e = stack.pop()
                self.set_visited(e)
            else:
                n = node.positon
                child = self.get_unvisited_child(n,stack) # list_remove_list(node.get_lower_node(),visited)

                if child == []:
                    e = stack.pop()
                    self.set_visited(e)
                    self.clear_visited(e,stack)
                    """
                    # 删除visited里面所有e的child
                    last_node = Node(e, self.street, self.direction)
                    lower_nodes = last_node.get_lower_node()
                    former_node_pos = stack[len(stack)-1]
                    former_node = Node(former_node_pos,self.street,self.direction)
                    former_node_child = former_node.get_lower_node()
                    nodes_need_to_remove = list_remove_list(lower_nodes,list_and_list(lower_nodes,former_node_child))
                    # 不是再前一个节点的child  不在stack里面？
                    visited = list_remove_list(visited, nodes_need_to_remove)
                  """
                else:
                    child_node = Node(child,self.street,self.direction)
                    stack.append(child_node.positon)
                    p = child_node.positon
                    self.set_visited(p)
                    node.set_visited()

        return ans



    def answer_to_standard_form(self,answer):

        ans = []

        for i in range(len(answer)):
            ans.append(list(answer[i]))
            for j in range(len(answer[i])):
                if len(answer[i][j])==2:
                    #print(answer[i][j])
                    ans[i][j] = answer[i][j]
                elif len(answer[i][j])==3:
                    answer[i][j].pop()
                    ans[i][j] = answer[i][j]

        return ans


    def reset_street(self):

        for i in range(len(self.street)):
            for j in range(1,len(self.street[i])):
                e = self.street[i][j]
                #print(e)
                self.set_unvisited(e)


    def get_path(self):
        #find the best answer(shortest) out of the all possible paths
        #print(self.street)
        #print("BEGIN")
        self.reset_street()
        #print(self.street)
        path_original = self.depthFirstSearch()
        #print(self.depthFirstSearch())
        #print("path original")
        #print(path_original)

        path = self.answer_to_standard_form(path_original)

        if path == []:
            ans = []
            print("Error: can't find a path")
        else:
            ans =path[0]
            l = calculate_length(ans)
            #print(l)
            for i in range(len(path)):
                if calculate_length(path[i])<l:
                    ans = path[i]
                    l = calculate_length(path[i])

        return ans

"""
def depthFirstSearch( start, goal ):
    stack = Stack()
    start.setVisited()
    stack.push( start )
    while not stack.empty():
        node = stack.top()
        if node == goal:
            return stack # stack には2頂点間の経路が入っている
        else:
            child = node.findUnvisitedChild()
            if child == none:
                stack.pop()
            else:
                child.setVisited()
                stack.push( child )
"""
