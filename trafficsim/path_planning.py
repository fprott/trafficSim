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
        for i in range(len(self.street)):
            if self.direction:
                for j in range(1,len(self.street[i])-1):
                    if self.street[i][j] == self.positon:
                        lower_node.append(self.street[i][j+1])
            else:
                for j in range(1,len(self.street[i]-1)):
                    if self.street[i][j] == self.positon:
                        lower_node.append(self.street[i][j-1])

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


    def get_unvisited_child(self,node,all_visited):

        ans =[]
        Node1 = Node(node,self.street,self.direction)
        a = Node1.get_lower_node()
        visited = list_and_list(a,all_visited)
        #find the visited nodes in the right layer
        if a == []:
            ans = []
        else:
            child = list_remove_list(a,visited)
            if child == []:
                ans = []
            else:
                ans = child[0]

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








    def depthFirstSearch(self):
        """start/end=[x,y]"""
        ans = []

        stack = []
        visited = []
        startNode = Node(self.start,self.street,self.direction)
        stack.append(startNode.positon)
        #start.set_visited()

        while stack != []:
            pos = stack[len(stack)-1]  #get the latest node in STACK
            node = Node(pos,self.street,self.direction)
            #print(ans)
            if node.positon == self.end:
                #return stack
                #print("find an answer:")
                #print(stack)
                path = tuple(stack)
                #此处stack堆栈不能直接保存
                ans = ans + [path]
                e = stack.pop()
                #print(ans)
                visited.append(e)
            else:
                #print(node.positon)
                #print(stack)
                #print(visited)
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


    def get_path(self):
        #find the best answer(shortest) out of the all possible paths
        path = self.depthFirstSearch()

        if path == []:
            print("Error: can't find a path")
        else:
            ans =path[0]
            l = calculate_length(ans)
            print(l)
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
