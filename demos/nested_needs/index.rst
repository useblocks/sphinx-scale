.. Nested needs documentation master file, created by
   sphinx-quickstart on Mon Apr 26 12:44:24 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Nested needs
============

Example of how needs can be nested / embedded and to make use of meta data from parent need.



.. req:: Parent requirement
   :id: REQ_001
   :status: open
   :style: green_border

   This is the parent requirement.

   It shall get some kind of a child requirement.


   .. req:: Child requirement
      :id: REQ_001_a
      :status: closed
      :style: blue_border

      I'm the child requirement.

      .. spec:: A spec for the child requirement
         :id: REQ_001_a_a
         :main_req: [[copy("parent_need")]]
         :style: red_border

         I'm the the spec for the child requirement.

      Req child text after embedded spec.

   Req parent text after embedded child requirement.


Analysis
--------


.. needtable::
   :style: table
   :columns: id, title, parent_needs, child needs
