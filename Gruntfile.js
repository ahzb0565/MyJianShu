module.exports = function(grunt){
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            build : {
                files: {
                    'JianShu\\static\\dest\\jianshu.min.js': ['JianShu\\static\\src\\js\\**\\*.js', 'JianShu\\static\\src\\js\\*.js']
                }
            }
        },
        jshint: {
            all: ['Gruntfile.js', 'JianShu\\static\\src\\js\\*.js',  'JianShu\\static\\src\\js\\**\\*.js'],
            options: {
                jshintrc: '.jshintrc'
            }
        },
        watch: {
            build: {
                files: ['JianShu\\static\\src\\js\\*.js',  'JianShu\\static\\src\\js\\**\\*.js'],
                tasks: ['uglify', 'jshint'],
                options: {spawn: false}
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['uglify', 'jshint', 'watch']);
};