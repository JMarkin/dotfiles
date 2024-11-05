;extends

; sql
(
 call
  function: (attribute attribute: (identifier) @id (#match? @id "execute|read_sql|text|fetch|prepare|fetchrow"))
  arguments: (argument_list
     (string (string_content) @injection.content (#set! injection.language "sql"))
  )
)

(
 call
  function: (attribute attribute: (identifier) @id (#match? @id "execute|read_sql|text"))
  arguments: (argument_list
     (
      concatenated_string
      (string (string_content) @injection.content (#set! injection.language "sql"))
     )
  )
)
(
 call
  function: ((identifier) @id (#match? @id "text"))
  arguments: (argument_list
     (string (string_content) @injection.content (#set! injection.language "sql"))
  )
)
(
 call
  function: ((identifier) @id (#match? @id "text"))
  arguments: (argument_list
     (
      concatenated_string
      (string (string_content) @injection.content (#set! injection.language "sql"))
     )
  )
)

(assignment
            ((identifier) @_varx (#match? @_varx ".*sql$"))
            (string
                (string_content) @injection.content (#set! injection.language "sql")))

;lua
(assignment
            ((identifier) @_varx (#match? @_varx ".*lua$"))
            (string
                (string_content) @injection.content (#set! injection.language "lua")))


; rst
(
 function_definition
        (block
          (expression_statement
            (string
                (string_content) @injection.content (#set! injection.language "rst"))))
)

; js
(
assignment
            ((identifier) @_varx (#match? @_varx ".*js$"))
            (string
                (string_content) @injection.content (#set! injection.language "javascript"))
)

; css
(assignment
            ((identifier) @_varx (#match? @_varx ".*html$"))
            (string
                (string_content) @injection.content (#set! injection.language "html")))

; css
(assignment
            ((identifier) @_varx (#match? @_varx ".*css$"))
            (string
                (string_content) @injection.content (#set! injection.language "css")))

(call
          function: (attribute
              attribute: (identifier) @_idd (#eq? @_idd "style"))
          arguments: (argument_list
            (string (string_content) @injection.content (#set! injection.language "css"))))

; json
(call
          function: (attribute
              attribute: (identifier) @_idd (#eq? @_idd "loads"))
          arguments: (argument_list
            (string (string_content) @injection.content (#set! injection.language "json") ) ) )

(assignment
            ((identifier) @_varx (#match? @_varx ".*json$"))
            (string
                (string_content) @injection.content (#set! injection.language "json")))
