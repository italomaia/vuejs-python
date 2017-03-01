VueListModel = Vue.extend
  data: ->
    results: []
    count: 0
    new_posts: false

  mounted: ->
    el = $ @$el
    src = el.attr 'src'
    $.get(src).done (data) => @$data = data

    socket.on 'new posts', => Materialize.toast('New Post! Press F5 to update.', 3000)

# on document ready ...
$ -> $('[vue-list]').each -> new VueListModel
  # ES6 template string style (this is important!)
  delimiters: ['${', '}']
  el: this
