ダイアログテスト
================================================================

ダイアログテスト1
---------------------------
.. blockdiag::

  blockdiag {
   // Set node metrix
   node_width = 200;
   node_height = 100;

   A -> B;
  }

ダイアログテスト2
---------------------------
.. blockdiag::

  blockdiag {
    // Set span metrix
    span_width = 240;
    span_height = 120;

    A -> B, C;
  }

ダイアログテスト3
---------------------------
.. blockdiag::

  blockdiag {
    // Set fontsize
    default_fontsize = 24;

    A -> B;
  }

ダイアログテスト4
---------------------------
.. blockdiag::

  blockdiag {
    // set default shape
    default_shape = roundedbox

    A -> B;
  }

ダイアログテスト5
--------------------------
.. blockdiag::
  
  blockdiag {
   orientation = portrait

   A -> B -> C;
        B -> D;
  }

ダイアログテスト6
--------------------------
.. blockdiag::

  blockdiag {
    default_node_color = lightyellow;
    default_group_color = lightgreen;
    default_linecolor = magenta;
    default_textcolor = red;

    A -> B -> C;
        B -> D;
    group {
      C; D;
    }
  }
