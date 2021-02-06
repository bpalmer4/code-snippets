def finalise_plot(ax, **kwargs):
    """A function to automate the completion of simple 
       matplotlib plots, including saving it to file 
       and closing the plot when done.
       
       Arguments:
       - ax - required - a matplotlib axes object
       - matplotlib axes settings - optional - any/all of the 
         following : 
            title, xlabel, ylabel, xticks, yticks, 
            xticklabels, yticklabels, xlim, ylim, 
            xscale, yscale, 
       - lfooter - optional - string - left side chart footer
       - rfooter - optional - string - right side chart footer
       - tight_layout_pad - optional - float - tight layout padding
       - set_size_inches - optional - tuple of floats - plot size,
         defaults to (8, 4) if not set
       - save_as - optional - string - filename for saving
       - chart_directory - optional - string - chart directory for
         saving plot using the plot title as the name for saving.
         The save file is defined by the following string:
         f'{kwargs["chart_directory"]}{title}{save_tag}.{save_type}'
         [Note: assumes chart_directory has concluding '/' in it].
       - save_type - optional - string - defaults to 'png' if not set
       - save_tag - optional - string - additional name
       - show - whether to show the plot
       - display - whether to display the plot (from Jupyter Notebook)
       - dont_close - optional - if set and true, the plot is not 
         closed 
       
       Returns: None
    """

    # defaults
    DEFAULT_SET_SIZE_INCHES = (8, 4)
    DEFAULT_SAVE_TYPE = 'png'
    DEFAULT_TIGHT_PADDING = 1.2
    DEFAULT_SAVE_TAG = ''
    AXES_SETABLE = ('title', 'xlabel', 'ylabel', 'xticks', 'yticks', 
                    'xticklabels', 'yticklabels', 'xlim', 'ylim', 
                    'xscale', 'yscale',)
    OTHER_SETABLE = ('lfooter', 'rfooter', 'tight_layout_pad', 
                     'set_size_inches', 'save_as', 'chart_directory',
                     'save_type', 'save_tag', 'show', 'display',
                     'dont_close')
    
    # utility
    def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)
    
    # precautionary
    if 'title' not in kwargs:
        eprint('Warning: the plot title has not been set\n'
              '\tin the call to finalise_plot().')
    for arg in kwargs:
        if arg not in AXES_SETABLE and arg not in OTHER_SETABLE:
            eprint(f'Warning: the argument "{arg}" in the call\n'
                  '\tto finalise_plot() is not recognised.')
    
    # usual settings
    settings = {}
    for arg in kwargs:
        if arg not in AXES_SETABLE:
            continue
        settings[arg] = kwargs[arg]
    if len(settings):
        ax.set(**settings)
    
    fig = ax.figure
    
    # right footnote
    if 'rfooter' in kwargs and kwargs['rfooter'] is not None:
        fig.text(0.99, 0.005, kwargs['rfooter'],
            ha='right', va='bottom',
            fontsize=9, fontstyle='italic',
            color='#999999')
    
    # left footnote
    if 'lfooter' in kwargs and kwargs['lfooter'] is not None:
        fig.text(0.01, 0.005, kwargs['lfooter'],
            ha='left', va='bottom',
            fontsize=9, fontstyle='italic',
            color='#999999')

    # figure size
    if 'set_size_inches' in kwargs:
        size = kwargs['set_size_inches']
    else:
        size = DEFAULT_SET_SIZE_INCHES
    fig.set_size_inches(*size)
    
    # tight layout
    if 'tight_layout_pad' in kwargs:
        pad = kwargs['tight_layout_pad']
    else:
        pad = DEFAULT_TIGHT_PADDING
    fig.tight_layout(pad=pad)
    
    # save the plot to file
    # - save using the specified file name
    save_as = None
    if 'save_as' in kwargs:
        save_as = kwargs['save_as']
    
    # - save using a file name built from diretory-title-tag-type
    elif 'chart_directory' in kwargs:
        save_type = DEFAULT_SAVE_TYPE 
        if 'save_type' in kwargs:
            save_type = kwargs['save_type']
        save_tag = DEFAULT_SAVE_TAG
        if 'save_tag' in kwargs:
            save_tag = kwargs['save_tag']
        # file-system safe
        if 'title' in kwargs:
            title = kwargs['title'].replace('[:/]', '-')
        else:
            title = ''
        save_as = (f'{kwargs["chart_directory"]}{title}'
                   f'{save_tag}.{save_type}')

    # - warn if there is no saving arrangement
    else:
        eprint('Warning: in the call to finalise_plot()\n'
              '\tyou need to specify either save_as or\n'
              '\tchart_directory to save a plot to file.')

    if save_as:
        fig.savefig(save_as, dpi=125)
    
    # show the plot
    if 'show' in kwargs and kwargs['show']:
        plt.show()

    # display the plot (from Jupyter Notebook)
    if 'display' in kwargs and kwargs['display']:
        display(fig)

    # close the plot
    if 'dont_close' not in kwargs or not kwargs['dont_close']:
        plt.close()
    
    return None
