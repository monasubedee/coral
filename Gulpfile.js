const gulp = require( 'gulp' );
const sass = require( 'gulp-sass' );
const sassGlob = require( 'node-sass-glob-importer' );
const gulpSassGlob = require( 'gulp-sass-glob' );
const postcss = require( 'gulp-postcss' );
const mqpacker = require( 'css-mqpacker' );
const autoprefixer = require( 'autoprefixer' );
const postcssFlexbugsFixes = require( 'postcss-flexbugs-fixes' );
const sourcemaps = require( 'gulp-sourcemaps' );
const cachebust = require( 'gulp-cache-bust' );

gulp.task( 'compileSass', () => {
  const processors = [
    autoprefixer( {
      browsers: [ 'last 1 versions' ]
    } ),
    mqpacker(),
    postcssFlexbugsFixes()
  ];
  return gulp
    .src( './src/scss/**/*.scss' )
    .pipe( sourcemaps.init() )
    .pipe( gulpSassGlob() )
    .pipe(
      sass( {
        outputStyle: 'expanded',
        importer: sassGlob()
      } ).on( 'error', sass.logError )
    )
    .pipe( postcss( processors ) )
    .pipe( sourcemaps.write( 'maps' ) )
    .pipe( gulp.dest( 'bin/static/css/' ) );
});
gulp.task('compileSassBin', () => {
  const processors = [
    autoprefixer({
      browsers: ['last 1 versions']
    }),
    mqpacker(),
    postcssFlexbugsFixes()
  ];
  return gulp
    .src('./bin/static/ver2.1/scss/**/*.scss')
    .pipe(gulpSassGlob())
    .pipe(
      sass({
        outputStyle: 'expanded',
        importer: sassGlob()
      }).on('error', sass.logError)
    )
    .pipe(postcss(processors))
    .pipe(gulp.dest('./bin/static/ver2.1/css/'));
});

gulp.task( 'cacheBusting', () => {
  return gulp
    .src( './bin/templates/**/*.html', { base: './' } )
    .pipe(
      cachebust( {
        type: 'timestamp'
      } )
    )
    .pipe( gulp.dest( './' ) );
} );
gulp.task( 'compileProductionSass', () => {
  const processors = [
    autoprefixer( {
      browsers: [ 'last 1 versions' ]
    } ),
    mqpacker(),
    postcssFlexbugsFixes()
  ];
  return gulp
    .src( './src/scss/**/*.scss' )
    .pipe( gulpSassGlob() )
    .pipe(
      sass( {
        outputStyle: 'expanded',
        importer: sassGlob()
      } ).on( 'error', sass.logError )
    )
    .pipe( postcss( processors ) )
    .pipe( gulp.dest( 'bin/static/css/' ) );
} );

gulp.task( 'watchSass', () => {
  gulp.watch( [ 'src/**/*.scss' ], [ 'compileSass' ] );
} );

gulp.task( 'watchSassBin', () => {
  gulp.watch([ './bin/**/*.scss' ], [ 'compileSassBin' ] );
} );

gulp.task('dev', ['compileSass', 'watchSass', 'compileSassBin',  'watchSassBin']);
gulp.task( 'compileAndCacheBusting', [ 'compileProductionSass', 'cacheBusting' ] );
