VueListModel = Vue.extend
  data: ->
    items: []
    items_count: 0
    has_next: false
    has_prev: false
    next_num: null
    prev_num: null
    page: 0
    pages: 0
    total: 0

  mounted: ->
    el = $ @$el
    src = el.attr 'src'
    $.get(src).done (data) =>
      for k,v of data
        this[k] = v

    socket.on 'new posts', => Materialize.toast('New Post! Press F5 to update.', 3000)

# on document ready ...
$ -> $('[vue-list]').each -> new VueListModel
  # ES6 template string style (this is important!)
  delimiters: ['${', '}']
  el: this
